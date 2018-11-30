from bs4 import BeautifulSoup
import urllib3
import pprint


# URL to be scraped
URL = 'https://wiprodigital.com/'

# create HTTPResponse object using the above URL
http = urllib3.PoolManager()
urllib3.disable_warnings()
response = http.request(
    'GET', 
    URL,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)',
        'Accept-Language': 'en-US',
        'Accept-Encoding': 'text/html'
    })

# create Beautifulsoup object
# represents the document as a nested data structure
soup = BeautifulSoup(response.data, 'lxml')

# get all links from a tags from the soup
get_anchor_tags = soup.find_all('a')

# get all links and removes the url form the string
set_of_urls = set()
for tag in get_anchor_tags:
    if '#' not in tag['href'] and '[]' not in tag['href']:
        if tag['href'][-1] == "/":
            tag['href'] = tag['href'][0:-1]
        set_of_urls.add(tag['href'])

pprint.pprint(set_of_urls)