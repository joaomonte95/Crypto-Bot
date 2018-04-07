import json
import requests
from bs4 import BeautifulSoup

def get_request():
    request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    page_content = request.content
    soup = BeautifulSoup(page_content,"html.parser")
    api_json = json.loads(str(soup))
    return api_json
