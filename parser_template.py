from bs4 import BeautifulSoup
import requests

headers = {"accept-ranges": "bytes",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
url = "http://www.correctenglish.ru/theory/writing/contractions/"

req = requests.get(url, headers= headers)
src = req.text 

with open("index.html", "w") as file:
    file.write(src)

soup = BeautifulSoup(req, 'lxml')
print(src)
