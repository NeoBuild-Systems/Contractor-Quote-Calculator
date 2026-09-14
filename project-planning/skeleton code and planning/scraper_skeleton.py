import requests
from bs4 import BeautifulSoup
import csv
import time

# --- Configuration ---
# Target URL for a static, public-domain website (e.g., a simple Wikipedia page)
# NOTE: Always check the website's robots.txt and Terms of Service before scraping.
TARGET_URL = "http://quotes.toscrape.com/" 
OUTPUT_FILE = "scraped_quotes.csv"
DELAY_SECONDS = 1 # Ethical scraping: delay between requests

def fetch_page(url):
    """Fetches the HTML content of a given URL."""
    print(f"Fetching: {url}")
    
    # Ethical delay
    time.sleep(DELAY_SECONDS)
    
    # Set a User-Agent header to identify the scraper (ethical practice)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_quotes(html_content):
    """Parses the HTML content to extract quotes and authors."""
    if not html_content:
        return []

    # Initialize BeautifulSoup parser
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all quote containers using a CSS selector
    # The target site uses the class 'quote' for each quote block
    quote_elements = soup.find_all('div', class_='quote')
    
    scraped_data = []
    
    for quote_element in quote_elements:
        # Extract the quote text
        # The quote text is inside a <span> with class 'text'
        text = quote_element.find('span', class_='text').text
        
        # Extract the author name
        # The author name is inside a <small> with class 'author'
        author = quote_element.find('small', class_='author').text
        
        # Extract the tags (optional, for demonstration)
        tags = [tag.text for tag in quote_element.find('div', class_='tags').find_all('a', class_='tag')]
        
        scraped_data.append({
            'quote': text,
            'author': author,
            'tags': ', '.join(tags)
        })
        
    return scraped_data

def save_to_csv(data, filename):
    """Saves the extracted data to a CSV file."""
    if not data:
        print("No data to save.")
        return

    # Define the fieldnames for the CSV header
    fieldnames = ['quote', 'author', 'tags']
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Successfully saved {len(data)} records to {filename}")
    except IOError as e:
        print(f"Error saving to CSV: {e}")

def main():
    """Main function to run the scraper."""
    
    # 1. Fetch the HTML content
    html = fetch_page(TARGET_URL)
    
    # 2. Parse the content and extract data
    data = parse_quotes(html)
    
    # 3. Save the extracted data
    save_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
