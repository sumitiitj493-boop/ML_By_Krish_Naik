# We are going to use 3 URLs tcrape.
'''
URLs[
   https://dailyepaper.in/times-of-india-epaper-pdf-aug-2025/
   https://epaperwave.com/the-times-of-india-epaper-pdf-download/
   https://texviewer.herokuapp.com/
]
'''
import threading
import requests
from bs4 import BeautifulSoup

#List of URLs to scrape
urls = [
    "https://dailyepaper.in/times-of-india-epaper-pdf-aug-2025/",
    "https://epaperwave.com/the-times-of-india-epaper-pdf-download/",
    "https://chatgpt.com/"
]
def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print (f" Fetched {len(soup.text)} characters from {url}")
 
 # Create threads for each URL
threads = []
for url in urls:
     thread = threading.Thread(target=fetch_content, args=(url,))
     threads.append(thread)
     thread.start()
# Wait for all threads to complete
for thread in threads:
     thread.join()

print("Web scraping completed.")  
