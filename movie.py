import requests
import json
import urllib.request # API로 요청을 올바르게 보내기 위해서 ipipmport함 

headers = {
    'Host' : 'openapi.naver.com',
    'User-Agent' : 'curl/7.49.1',
    'Accept': '*/*',
    'X-Naver-Client-Id' : 'LhnxEFBFtfU_t4FCpTNw',
    'X-Naver-Client-Secret': 'dl1RIQJwGl',
}

url= 'https://openapi.naver.com/v1/search/movie.json'

params = {
    'query' : '어벤져스',
}

response = requests.get(url, headers=headers, params=params)
jsonObj = json.loads(response.text)
title = jsonObj["items"][1]["title"]
link = jsonObj["items"][1]["link"]
director = jsonObj["items"][1]["director"]
title = title.replace("<b>", "")
title = title.replace("</b>", "")

director = director.replace("|", " ")
print(title)
print(link)
print(director)


client_id = "LhnxEFBFtfU_t4FCpTNw" # 위에서 받은 클라이언트 ID 넣어줌
client_secret = "dl1RIQJwGl" # 위에서 받은 시크릿키 넣어줌

encText = urllib.parse.quote("기생충")
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id) # API주소로 요청을 보낼 때 헤더에 클라이언트 ID를 꼭 넣어줘야함
request.add_header("X-Naver-Client-Secret",client_secret) # API주소로 요청을 보낼 때 헤더에 시크릿키를 꼭 넣어줘야함

response = urllib.request.urlopen(request) # API주소로부터 받은 API객체를 response에 넣는다.
rescode = response.getcode() # HTTP 코드 200은 성공을 의미
if(rescode==200): # 성공일 때
    response_body = response.read()
    response_body = response_body.decode('utf-8') # 한국어로 정보를 얻기 위해 utf-8로 디코딩 함
    response_body = response_body.replace('<b>', ' ')
    response_body = response_body.replace('</b>',' ')
    response_body = response_body.replace('|', ' ')
    print(response_body)
else: # 실패일 때
    print("Error Code:" + rescode)