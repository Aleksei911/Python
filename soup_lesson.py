from bs4 import BeautifulSoup
import requests

req = requests.get("https://browser-info.ru/").text
print(req)

soup = BeautifulSoup(req, "lxml")