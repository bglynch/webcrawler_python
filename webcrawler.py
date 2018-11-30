from bs4 import BeautifulSoup
import urllib3
import pprint
import re


# URL to be scraped
URL = 'https://wiprodigital.com/'

def format_html_to_xml_soup(url):
    '''
    takes in webpage url
    returns the html code for that url
    '''
    # create HTTPResponse object using the above URL
    http = urllib3.PoolManager()
    urllib3.disable_warnings()
    response = http.request(
        'GET', 
        url,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3)',
            'Accept-Language': 'en-US',
            'Accept-Encoding': 'text/html'
        })
    
    # create Beautifulsoup object
    # represents the document as a nested data structure
    return BeautifulSoup(response.data, 'lxml')

def get_all_links_from_url(url):
    '''
    takes in a webpage url
    extracts all the anchor tag links as a set
    parses the set for # links and radio button links
    returns a set of urls as strings
    '''
    soup = format_html_to_xml_soup(url)
    
    # get all links from a tags from the soup
    get_anchor_tags = soup.find_all('a')

    # get all links and removes the url form the string
    set_of_urls = set()
    for tag in get_anchor_tags:
        if '#' not in tag['href'] and '[]' not in tag['href']:
            if tag['href'][-1] == "/":
                tag['href'] = tag['href'][0:-1]
            set_of_urls.add(tag['href'])
    
    return set_of_urls

def split_link_to_domain_and_external(set_of_urls):
    # Split links into Internal and External Links
    internal_links = set()
    external_links = set()
    
    for link in set_of_urls:
        if 'https://wiprodigital.com' in link:
            internal_links.add(link)
        else:
            external_links.add(link)
    
    return internal_links, external_links

def get_image_links_from_url(url):
    '''
    extract all image links from a given url
    '''
    soup = format_html_to_xml_soup(url)
    
    regex = r"(\'|\")https://\S*\.(jpg|png|jpeg|gif)(\'|\")"
    text_str = str(soup)
    matches = re.finditer(regex, text_str, re.MULTILINE)
    
    image_links = set()
    for match in matches:
        image_links.add(match.group())
    
    return image_links

def get_css_links_from_url(url):
    soup = format_html_to_xml_soup(url)
    
    # Get all css files from URL
    css_links = [link_tag["href"] for link_tag in soup.findAll('link', rel="stylesheet")]
    
    return css_links

def get_javascript_links_from_url(url):
    soup = format_html_to_xml_soup(url)
    
    # Get all js links from URL
    js_links = [script_tag['src'] for script_tag in soup.find_all('script') if script_tag.get('src')]
    
    return js_links
