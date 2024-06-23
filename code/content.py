import requests

for page in range(1,6):
    # url = f'https://api.bilibili.com/x/v2/reply/wbi/main?oid=1355131651&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=16d804d7200eee4bd67204cfc68a7c1d&wts=1717305261'
    url =f'https://api.bilibili.com/x/v2/reply/wbi/main?oid=1852698584&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=67f2d82e5c9e90b348b5d587494c90a0&wts=1717321963'
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
            }
    response =requests.get(url=url,headers=headers)
    for index in response.json()['data']['replies']:
        content= index['content']['message']
        with open('评论.txt',mode='a',encoding='utf-8')as f:
                f.write(content)
                f.write('\n')
                print(content)