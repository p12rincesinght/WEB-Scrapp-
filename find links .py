from bs4 import BeautifulSoup
import requests
import re
  
  
# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text
  
    

url_to_scrape = "https://practice.geeksforgeeks.org/courses/"
  
# create document
html_document = getHTMLdocument(url_to_scrape)
  
# create soap object
soup = BeautifulSoup(html_document, 'html.parser')
  
  
# find all the anchor tags with "href" 
# attribute starting with "https://"
for link in soup.find_all('a', 
                          attrs={'href': re.compile("^https://")}):
    # display the actual urls
    print(link.get('href')) 