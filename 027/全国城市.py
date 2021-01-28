import requests
from lxml import etree
if __name__ =="__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    response = requests.get(url=url,headers=headers)
    page_text = response.text
    #print(response.encoding)
    tree = etree.HTML(page_text)
    '''
    host_li_list = tree.xpath('//div[@class="bottom"]//li')
    all_city_names = []
    #热门城市
    for li in host_li_list:
        host_city_name = li.xpath('./a/text()')[0]
        all_city_names.append(host_city_name)
    #全部城市
    city_names = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/li')
    for li in city_names:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))
    '''
    host_li_list = tree.xpath('//div[@class="bottom"]//li')
    all_city_names = []
    #热门城市
    for li in host_li_list:
        host_city_name = li.xpath('./a/text()')[0]
        all_city_names.append(host_city_name)
    #全部城市
    city_names = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/li')
    for li in city_names:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)
    #print(all_city_names,len(all_city_names))
    with open('./cityLibs.txt','w',encoding='utf-8') as fp:
        fp.write(str(all_city_names))

