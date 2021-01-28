import requests
from lxml import etree
import os
if __name__ =="__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    html_url = 'https://sc.chinaz.com/jianli/free.html'
    if not os.path.exists('./jianli'):
        os.mkdir('./jianli')

    page_text = requests.get(url=html_url,headers=headers).text
    tree = etree.HTML(page_text)
    #拿到最外层的主div
    main_list =tree.xpath('//*[@id="container"]/div')
    #print(all_div_list)
    for a_href_list in main_list:
        #简历超链接  用于发请求下载
        a_hrefs = "https:" + a_href_list.xpath('./a[1]/@href')[0]
        #简历名称  用于存储时的文件名
        names = a_href_list.xpath('./p/a/text()')[0].encode('iso-8859-1').decode('utf-8')
        #获取下载页面
        download_page_text = requests.get(url=a_hrefs,headers=headers).text
        #实例化新的tree 叫做download_tree
        download_tree = etree.HTML(download_page_text)
        #获取每个下载页面的下载地址
        download_url = download_tree.xpath('//*[@id="down"]/div[2]/ul/li[3]/a/@href')[0]
        #对每一个下载地址发请求
        jianli_data = requests.get(url=download_url,headers=headers).content
        jianli_path = './jianli/' + names + '.rar'
        with open(jianli_path,'wb') as fp:
            fp.write(jianli_data)
            print(names,'下载成功')








