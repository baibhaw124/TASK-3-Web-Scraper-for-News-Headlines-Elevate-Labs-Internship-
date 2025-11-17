import requests
from bs4 import BeautifulSoup

# Function to scrape headlines from a given news website
def scrape_headlines(url):
    try:
        ''' Adding headers to pretend we are a real browser
        User-Agent' helps avoid blocking from websites'''
        
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # Sending GET request to the URL
        response = requests.get(url, headers=headers)

        # Raises an error if the request was unsuccessful (like 404 )
        response.raise_for_status()

        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all <h2> headlines.
        headlines = [h2.text.strip() for h2 in soup.find_all('h2') if h2.text.strip()]

        # Returning the list of extracted headlines
        return headlines

    except Exception as e:
        # If any error happens (network issue, parsing error, etc.)
        print("Error:", e)
        return []


if __name__ == "__main__":
    url = "https://www.thehindu.com/"  #Here You can Choose any News Website as per your recomandation

    print("Fetching headlines...")
    # Calling the function to scrape headlines
    titles = scrape_headlines(url)

    # If headlines were extracted successfully
    if titles:
        print(f"Collected {len(titles)} headlines.")

        # Saving the headlines into a text file
        

