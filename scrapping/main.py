import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    # Step 1: Make an HTTP request to the website
    url = 'https://shanvi.co/'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch the web page. Status code: {response.status_code}")
        return

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 3: Extract data (e.g., quotes and authors)
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # Step 4: Print the scraped data
    for i in range(len(quotes)):
        print(f"Quote: {quotes[i].text.strip()}")
        print(f"Author: {authors[i].text.strip()}")
        print("---")

if __name__ == "__main__":
    scrape_quotes()
