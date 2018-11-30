# Brian Lynch - Simple Web Crawler
## Summary

This is a simple webcrawler for extracting data from a given domain.  
Its returns a simple html page showing all the links extracted from the domain.  
These include:
- links to other pages on the same domain
- links to external URLs
- links to static content
    - images
    - css
    - javascript

## Technologies Used
| Tech        | Description          
| ------------- |:-------------| 
| [Python 3.6](https://www.python.org/downloads/release/python-360/)        | Language used to create the crawler | 
| [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)    | Python library for pulling data out of HTML and XML files |  
| [lxml](https://lxml.de/)              | Library for processing XML and HTML in the Python language | 
| [urllib3](https://urllib3.readthedocs.io/en/latest/)           | Powerful, sanity-friendly HTTP client for Python | 
IDE used to build: [AWS Cloud9](https://aws.amazon.com/cloud9/?origin=c9io)  
## Deployment
To run the code locally, please follow the instructions below.  
(Note: **Python 3.6** must be installed for be able to run this program)
1. Git clone this repository to a local directory:  
```
git clone https://github.com/bglynch/webcrawler_python.git
```
2. Install the packages required to run this project
```
pip install -r requirements.txt
```
3. Open the **data_to_html.py** file and update the URL to a website of your choice
```
URL = 'your-website-url'
```
4. Run the **data_to_html** file:
```
python data_to_html.py
```
5. Open **sitemap.html** in your browser

## Build Details
### Build Plan
#### Stage 01
- [x] Take Starting URL as the web domain home page
- [x] Get all the links from a home page
- [x] Split links into INTERNAL and EXTERNAL
- [x] Get all images from the home page
- [x] Get all css from the home page
- [x] Get all javascript from the home page
- [x] Write these to a Home Page Sitemap
  
#### Stage 02
- [] From the Starting URL get all the links in the domain
- [] Split links into INTERNAL and EXTERNAL
- [] Using the links from the INTERNAL, get all images in the domain
- [] Using the links from the INTERNAL, get all css in the domain
- [] Using the links from the INTERNAL, get all javascript in the domain
- [] Write these to a Domain Page Sitemap

### Bugs
- image_links in wrong format, inside double set of quotes
    - currently: '"https://s17776.pcdn.co/wp-content/uploads/2016/03/home-cta.png"' 
    - correct: "https://s17776.pcdn.co/wp-content/uploads/2016/03/home-cta.png"


### Things to be done
- Complete Build Plan
- Fix any known bugs
- Look for better method to display data as html
    - so it looks similar to **scratchpad/mockup.html**
    - possible update the dataset from a set to a dict


