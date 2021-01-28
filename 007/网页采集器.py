import requests
if __name__ =="__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    kw = input('enter a word :')
    param = {
        'query':kw
    }

    page_text = requests.get(url=url,params=param,headers=headers).text
    fileName = kw+'.html'

    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'successful')




