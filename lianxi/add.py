import requests
import unittest
import datetime
import json

#heads={"User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"}
url = "https://bplussit.sinosun.com:18280/follow/v1/deleteItem"
#url="https://bpsandbox.sinosun.com:18194/bp/train/query"
#date = ((datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y-%m-%d"))
i=927663
while i<927674:
    data={
    "userId":"25966",
    "companyId":"12",
    "channelId":"1",
    "skus": [
        {
            "sku":i,
            "supplierId": 1
        }
    ]
        }
    i=i+1
#get_url = url +'?sso={"TGC":"b010e7627bbb47688d997a54b234d233","TerType":"1","ProdId":"1","CpyId":"12","UaId":"25966","AppletUaId":null,"ProductChannel":null,"UserPhone":null}'
    headers={"Content-Type":"application/json;charset=UTF-8"}

    req = requests.post(url,headers=headers, data=json.dumps(data))

#print(req.status_code)
#print(req.text)
    aa = json.loads(req.text)
#print(aa)
    print(aa)
    print(i)