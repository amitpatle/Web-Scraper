
```markdown
# Web Scraper Project

## Overview
This project demonstrates a simple web scraper implemented using HTML for the frontend, Python (Flask) for the backend, and web scraping libraries (BeautifulSoup and Pytube) for extracting images, audio, and video content from a given URL.

## Features
- **Frontend**: A user-friendly HTML interface with a form for entering the target URL.
- **Backend**: Flask server handling URL input, web scraping, and file saving.
- **Scraping**: Extracts images, audio, and video content from the specified webpage.
- **Saving**: Downloads and saves the scraped files in their original formats (images, audio, and video).

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/amitpatle/web-scraper.git
   cd web-scraper
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your web browser and visit `http://127.0.0.1:5000/` to access the web scraper interface.

## Usage
1. Enter the target URL in the form and click "Scrape."
2. The scraper will extract images, audio, and video content from the webpage.
3. Files will be saved in the `static` folder (images, audio, and video subdirectories).

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Web Scraping**: BeautifulSoup (Python)
- **Video Download**: Pytube (Python)

## Disclaimer
Web scraping may have legal and ethical implications. Ensure that you have the right to scrape content from the target website and comply with its terms of service.

## License
This project is licensed under the [MIT License](LICENSE).
