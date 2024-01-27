import requests
from bs4 import BeautifulSoup

def scrape_bbc_news_titles(url, num_articles=5):
    # Send a request to the BBC News website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing the news titles
        title_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')

        # Extract the titles of the top N articles
        top_titles = [title.text.strip() for title in title_elements[:num_articles]]

        return top_titles
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# BBC News URL
bbc_url = 'https://www.bbc.com/news'

# Scrape and print the top 5 news article titles
top_news_titles = scrape_bbc_news_titles(bbc_url)
if top_news_titles:
    print("Top 5 news articles from BBC News:")
    for i, title in enumerate(top_news_titles, start=1):
        print(f"{i}. {title}")
