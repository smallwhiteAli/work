import requests
import json
'''
    param = {
        'type':'  5',
        'interval_id':'   100:90',
        'action':'',
        'start':'   0',
        'limit':'   20'
    }
从谷歌抓包工具里复制来的参数有空格
'''

if __name__ =="__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'0',#从库中第几部电影开始
        'limit':'20',#一次取多少个
    }
    response = requests.get(url=url,params=param,headers=headers)

    print(response.json())

    list_data = response.json()
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('over!')