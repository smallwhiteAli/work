import requests
url = 'https://www.sogou.com/'
page_txt = requests.get(url=url).text
print(page_txt)
with open('./sougou.html','w',encoding='utf-8') as fp:
	fp.write(page_txt)
print('end')