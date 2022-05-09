import requests
import json
 
headers={
    'Host': 'openapi.naver.com',
    'User-Agent':'curl/7.49.1',
    'Accept':'*/*',
    'X-Naver-Client-Id':'xxxxxxxxxxx',
    'X-Naver-Client-Secret':'xxxxxxxx',
 }

url='https://openapi.naver.com/v1/search/movie.json'
params={'query':'태극기 휘날리며',}
response=requests.get(url,headers=headers,params=params)
data=response.json()

title=data['items'][0]['title'].strip("</b>")
link=data['items'][0]['link']
director=data['items'][0]['director'].split('|')[0]

print("영화 제목 :",title)
print("링크 :",link)
print("감독 :", director)