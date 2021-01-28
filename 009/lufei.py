import requests
if __name__ == "__main__":
    #指定ajax-get请求的url（通过抓包进行获取）
    url = 'https://movie.douban.com/j/chart/top_list?'
    #定制请求头信息，相关的头信息必须封装在字典结构中
    headers = {
        #定制请求头中的User-Agent参数，当然也可以定制请求头中其他的参数
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
    #定制get请求携带的参数(从抓包工具中获取)
    param = {
        'type':'5',
        'interval_id':'100:90',
        'action':'',
        'start':'0',
        'limit':'20'
    }
    #发起get请求，获取响应对象
    response = requests.get(url=url,headers=headers,params=param)
    #获取响应内容
    print(response.json())