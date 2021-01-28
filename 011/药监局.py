import requests
import json
if __name__ =="__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []#获取所有企业的id
    all_data_list = []#存储所有企业的详情数据
    for page in range(1,5):
        data = {
            'on':'true',
            'page':page,
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
            'applysn':'',
        }

        json_id = requests.post(url=url,headers=headers,data=data).json()
        for dic in json_id['list']:
            id_list.append(dic['ID'])
    #获取详情页的数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url,data=data,headers=headers).json()
        #print(detail_json)
        all_data_list.append(detail_json)


    fp = open('./alldata.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!')



