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
import pprint

domain = 'https://wiprodigital.com/'

# Create sets
start_urls = get_all_links_from_url(domain)
all_urls = set()
crawled_urls = set()
external_urls = set()

# Parse out the external links
for link in start_urls:
    if 'https://wiprodigital.com' in link:
        all_urls.add(link)
    else:
        external_urls.add(link)

uncrawled_urls = all_urls - crawled_urls

print(len(all_urls))
print('')
print(len(external_urls))
print('')
print(len(uncrawled_urls))

while len(uncrawled_urls) > 0:
    i = 0
    for link in uncrawled_urls:
        i += 1
        print(f"{i} / {len(uncrawled_urls)}: {link}")
        link_urls = get_all_links_from_url(link)
        crawled_urls.add(link)
        for url in link_urls:
            if 'https://wiprodigital.com' in url:
                all_urls.add(url)
            else:
                external_urls.add(url)
            
    uncrawled_urls = all_urls - crawled_urls
    print(uncrawled_urls)
    
    print(len(all_urls))
    print('')
    print(len(external_urls))
    print('')
    print(len(uncrawled_urls))



print('')
print('========== INTERNAL URLS ============')
print('')
pprint.pprint(sorted(all_urls))
print('')
print('========== EXTERNAL URLS ============')
print('')
pprint.pprint(sorted(external_urls))