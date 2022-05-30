from bs4 import BeautifulSoup
import requests


amazon  = "https://www.amazon.com/s?k={}" # Add search parameters after the search query
flipkart = "https://www.flipkart.com/search?q" # Add search parameters after the search query
# Add search parameters after the search query

# specifying user agent, You can use other user agents
# available on the internet
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(amazon.format("macbook"),headers=HEADERS) # Get the HTML Text of the requested site

soup = BeautifulSoup(webpage.content,'lxml')

print(soup.find_all("span", class_ = "a-text-normal")[2].text)
price = [i.text for i in soup.find_all("span", class_ = "a-offscreen")]
print(price)