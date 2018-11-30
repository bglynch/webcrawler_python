from webcrawler import (
    format_html_to_xml_soup,
    get_all_links_from_url,
    split_link_to_domain_and_external,
    get_image_links_from_url,
    get_css_links_from_url,
    get_javascript_links_from_url
    )
        
URL = 'https://wiprodigital.com'

set_of_urls = get_all_links_from_url(URL)

internal_links, external_links = split_link_to_domain_and_external(set_of_urls)

image_links = get_image_links_from_url(URL)

css_links = get_css_links_from_url(URL)

js_links = get_javascript_links_from_url(URL)

    
# PRINT THE ABOVE LISTS TO A HTML FILE IN UNORDERED LISTS
with open('sitemap.html', 'w') as myFile:
    myFile.write('<html>')
    myFile.write('<body>')
    myFile.write('<h1>Sitemap for https://wiprodigital.com</h1>')
    myFile.write('<h2>Internal Links</h2>')
    
    for url in sorted(internal_links):
        myFile.write(f"<ul><a href={url}><li>{url.replace(URL, '')}</li></a></ul>")

    myFile.write('<h2>External Links</h2>')
    for url in sorted(external_links):
        myFile.write(f"<ul><a href='{url}'><li>{url}</li></a></ul>")
    
    myFile.write('<h2>Static Links</h2>')
    
    myFile.write('<h3>Image Links</h2>')
    for url in sorted(image_links):
        myFile.write(f"<ul><a href={url}><li>{url}</li></a></ul>")
    
    myFile.write('<h3>CSS Links</h2>')
    for url in css_links:
        myFile.write(f"<ul><a href='{url}'><li>{url}</li></a></ul>")
    
    myFile.write('<h3>Javascript Links</h2>')
    for url in js_links:
        myFile.write(f"<ul><a href='{url}'><li>{url}</li></a></ul>")
    
    myFile.write('</body>')
