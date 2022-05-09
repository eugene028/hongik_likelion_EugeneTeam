import re
from urllib import response
import requests
import json

headers = {
    'Host': 'openapi.naver.com',
    'User-Agent': 'curl/7.49.1',
    'Accept': '*/*',
    'X-Naver-Client-id': '',
    'X-Naver-Client-secret': '',
}

url = 'https://openapi.naver.com/v1/search/movie.json'
params = {'query': '스파이더맨', }

response = requests.get(url, headers=headers, params=params)
# print(response.text)

jsonObect = response.json()
movie_data = jsonObect['items'][0]

# replace 함수 사용
title = movie_data['title'].replace("<b>", "").replace("</b>", "")
link = movie_data['link']
director = movie_data['director'].replace("|", " ")

print("Title: ", title)
print("Link: ", link)
print("Director: ", director)
