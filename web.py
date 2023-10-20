import requests
from bs4 import BeautifulSoup
import urllib

# Function to download an image or video
def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# URL of the website you want to scrape
website_url = 'https://example.com'

# Send an HTTP GET request to the website
response = requests.get(website_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Scrape images
    img_tags = soup.find_all('img')
    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            img_filename = img_url.split('/')[-1]
            download_file(img_url, img_filename)
    
    # Scrape videos (replace 'video' with the appropriate HTML tag for videos)
    video_tags = soup.find_all('video')
    for video in video_tags:
        video_url = video.get('src')
        if video_url:
            video_filename = video_url.split('/')[-1]
            download_file(video_url, video_filename)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
