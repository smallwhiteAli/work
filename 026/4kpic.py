import requests
from lxml import etree
import os
'''
    1.处理中文乱码的解决方案
    response.encoding = 'gbk'

    通用！！！！
    2.处理中文乱码的解决方案
    img_name = img_name.encode('iso-8859-1').decode('gbk')
'''
if __name__ =="__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    url = 'http://pic.netbian.com/4kmeinv/'
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    #手动设定响应数据的编码
    response = requests.get(url=url,headers=headers)
    page_text = response.text

    #数据解析：src 和 alt属性
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        #print(img_name,img_src)
        #持久化存储
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功')


