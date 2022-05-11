import json
import urllib.request


client_id = "EIhfE3a2NQ0EtEiQ8DGl"
client_secret = "ftfapR6mwj"

query = "?query="+urllib.parse.quote(input("질의 : "))  # 옵션!

url = "https://openapi.naver.com/v1/search/movie.json"
url_query = url+query
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)

rescode = response.getcode()

if(rescode == 200):  # 보통 200이면 성공이라고 한다고..
    response_body = response.read()
    # utf-8로 디코딩한 것을 json형태로 불러오기.
    response_body = json.loads(response_body.decode('utf-8'))

else:
    print("Error code:"+rescode)

items = response_body.get("items")  # items키가 가리키는 value가 정보를 담고 있는 딕셔너리
movie_serarch = []
for item in items:
    dic = {}
    dic["title"] = item.get("title").replace(
        "<b>", "").replace("</b>", "")  # 태그 제거하기
    dic["link"] = item.get("link")
    dic["director"] = item.get('director').split('|')[0]
    dic["pubDate"] = item.get('pubDate')
    movie_serarch.append(dic)

for item in movie_serarch:

    print('\n\n'+'title : '+item['title'], '\n')
    print('link : '+item['link'], '\n')
    print('director : '+item['director'], '\n')
    print('pubDate : '+item['pubDate'], '\n\n')
