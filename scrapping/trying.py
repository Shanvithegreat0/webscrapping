import requests
from bs4 import BeautifulSoup


def scrape_and_save_data():
    # Step 1: Make an HTTP request to the website
    url = 'https://shanvi.co/'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch the web page. Status code: {response.status_code}")
        return

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 3: Extract data from <div> tags with class "name"
    name_divs = soup.find_all('div', class_='name')

    # Step 4: Extract and save the raw text data
    raw_data = ""
    for name_div in name_divs:
        raw_data += f"Raw Data: {name_div.get_text(strip=True)}\n{'=' * 50}\n"

    # Step 5: Print or save the raw data to a text file
    print(raw_data)

    # Save raw data to a text file
    with open('raw_data.txt', 'w', encoding='utf-8') as file:
        file.write(raw_data)


if __name__ == "__main__":
    scrape_and_save_data()
