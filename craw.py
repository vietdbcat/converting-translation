import requests 
from bs4 import BeautifulSoup 
import json
from tqdm import tqdm
import os

url = "https://truyentiki.top/the-loai/110"
print("Fetching the webpage...")

try:
    # Fetch the webpage
    r = requests.get(url, timeout=10)
    r.raise_for_status()  # Raise an HTTPError for bad responses
    print("Webpage fetched successfully.")
    
    
    s = BeautifulSoup(r.content, "html.parser")

    stories = s.find_all("div", class_="row")
    for story in stories:
        a = story.find("a")
        title = a["title"]
        href = a["href"]
        
        re = requests.get(url+href, timeout=10)
        so = BeautifulSoup(r.content, "html.parser")
        
        div = so.find_all("div", class_="container")
        print(len(div))
        break
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the webpage: {e}")
