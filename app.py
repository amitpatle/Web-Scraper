from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url']
    images, audio, video = scrape_website(url)
    save_files(images, 'images')
    save_files(audio, 'audio')
    save_videos(video, 'video')
    return jsonify({'message': 'Scraping and saving completed successfully.'})

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    images = [img['src'] for img in soup.find_all('img', src=True)]
    audio = [audio['src'] for audio in soup.find_all('audio', src=True)]

    # Extract video URLs from both iframe and video tags
    video = []
    video.extend([video['src'] for video in soup.find_all('video', src=True)])
    video.extend([iframe['src'] for iframe in soup.find_all('iframe', src=True)])

    return images, audio, video

def save_files(file_urls, folder):
    if not os.path.exists(f'static/{folder}'):
        os.makedirs(f'static/{folder}')

    for file_url in file_urls:
        try:
            response = requests.get(file_url, stream=True)
            filename = os.path.join('static', folder, os.path.basename(file_url))

            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
        except Exception as e:
            print(f"Error saving file {file_url}: {e}")

def save_videos(video_urls, folder):
    if not os.path.exists(f'static/{folder}'):
        os.makedirs(f'static/{folder}')

    for video_url in video_urls:
        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(file_extension='mp4').first()
            filename = os.path.join('static', folder, f'{yt.title}.mp4')
            stream.download(filename)
        except Exception as e:
            print(f"Error saving video {video_url}: {e}")

if __name__ == '__main__':
    app.run(debug=True)
