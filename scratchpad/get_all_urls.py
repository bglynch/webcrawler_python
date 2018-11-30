'''
=========================
PLAN

4 different sets needed
 - all_urls
 - crawled_urls
 - uncrawled_urls
 - external_urls
=========================

int_link1 = internal url link
ext_link1 = external url link

all_urls - contain all the external links found
crawled_urls - contain all the urls that have been crawled for links
uncrawled_urls - will be lthe difference between all_urls and crawled_urls
external_urls - any external url found while crawling will be add here

method - keep crawling until uncrawled_urls is an empty set

'''
from webcrawler_test import (
    format_html_to_xml_soup,
    get_all_links_from_url,
    )

domain = 'https://wiprodigital.com/'

# Create sets
all_urls = set()
crawled_urls = set()
uncrawled_urls = set()
external_urls = set()
    