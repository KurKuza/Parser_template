from bs4 import BeautifulSoup
import requests

headers = ["User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"]

# Получение контента
q = requests.get(url)
result = q.content

# lxml тип парсинга
soup = BeautifulSoup(result, 'lxml')