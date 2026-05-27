import urllib.request
import datetime
import json

client_id = 'qU7Vv0lpL6Vn_xp0A_M5'
client_secret = 'BqTjXFOz8m'

# NAVER에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS!!')
            # print(f'response data: {response.read().decode('utf-8')}')
            # decode란 바이트(byte) 코드를 문자열(string)로 변환하는 것.
            return response.read().decode('utf-8')
    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None

# NAVER에서 데이터 검색 하는 녀석
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'   # news.json
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)
    
def main():
    node = 'news'   # 크롤링 하는 대상
    srcText = input('검색어 입력: ')
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    print(f'jsonResponse: {jsonResponse}')
    print(f'jsonResponse total: {jsonResponse['total']}')
    print(f'jsonResponse items 0: {jsonResponse['items'][0]}')
    print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}')

if __name__ == '__main__':
    main()