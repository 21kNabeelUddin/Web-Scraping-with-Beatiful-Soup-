# Web-Scraping-with-Beatiful-Soup

there are currnetly two versions of the code

1.for scraping data off the internet

2.for scraping images off the internet

>MAKE SURE TO RUN THE FOLLOWING COMMANDS IN CMD FIRST

1.pip install BeautifulSoup4

2.pip install lxml


## Overview

This project is a web scraping tool built in Python that extracts data from web pages. It demonstrates how to scrape web content, including text and images, and save it to a structured format like a CSV file. The tool is versatile and can be customized to scrape different types of data from various websites.

## Features

Extract headlines, summaries, and image URLs from web pages.

Download and save images locally.

Automatically navigate through multiple pages of a website.

Save scraped data in a CSV file for further analysis.

## Technologies Used

Python

BeautifulSoup (for HTML parsing)

Requests (for HTTP requests)

CSV (for data storage)

OS (for file management)

## How It Works

Scraping Text Data: The tool uses BeautifulSoup to parse the HTML of a webpage, extract specific elements (e.g., headlines, summaries), and save them to a CSV file.

Image Downloading: It identifies image URLs, downloads the images, and saves them locally.

Pagination Handling: Automatically navigates through multiple pages using the pagination structure of the website.

## Installation

Clone the repository:
```bash
git clone https://github.com/21kNabeelUddin/Web-Scraping-with-Beatiful-Soup-.git
```
Navigate to the project directory:
```bash
cd Web-Scraping-with-Beatiful-Soup-
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage

Open the scrape.py file and replace the URL variable with the website you want to scrape.

Customize the HTML tags and class names in the code to match the structure of your target website.

Run the script:

python scrape.py

Scraped data will be saved to a file named data.csv, and images will be downloaded into an images/ folder.
