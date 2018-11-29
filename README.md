# Brian Lynch - Simple Web Crawler
## Summary
This is a simple webcrawler for extracting data from a given domain.  
Its returns a simple html page showing all the links extracted from the domain.  
These include:
- links to other pages on the same domain
- links to external URLs
- links to static content sunch as images

## Technologies Used
| Tech        | Description          
| ------------- |:-------------| 
| [Python 3.6](https://www.python.org/downloads/release/python-360/)        | Language used to create the crawler | 
| [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)    | Python library for pulling data out of HTML and XML files |  
| [lxml](https://lxml.de/)              | Library for processing XML and HTML in the Python language | 
| [urllib3](https://urllib3.readthedocs.io/en/latest/)           | Powerful, sanity-friendly HTTP client for Python | 

## Deployment
To run the code locally, please follow the instructions below.  
(Note: Python 3 must be installed for be able to run this program)
1. Git clone this repository to a local directory:  
```
git clone https://github.com/bglynch/webcrawler_python.git
```
2. Install the packages required to run this project
```
pip install -r requirements.txt
```

