import requests
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)





player_name = "Michael Jordan"
first_name = player_name.split(" ")[0]
last_name = player_name.split(" ")[1]
image_url = "https://en.wikipedia.org/wiki/"+first_name+"_"+last_name
request = requests.get(image_url)
soup4 = BeautifulSoup(request.text, 'html.parser')
result = soup4.find_all(attrs={'class','infobox vcard'})

url_image_scraped = "https://" + result[0].table.img.get("src").replace("//","",1)
