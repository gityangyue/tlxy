#!/usr/bin/env python3
import requests

for i in range(1):
    try:
        url = 'http://172.16.90.113/xmlService'
        #url = 'http://172.16.90.'+str(i)+'/xmlService'
        myData = open("FanvilConfiguration.xml", encoding="utf-8").read()
        myHeaders = {'Content-Type': 'text/xml',}

        rsp = requests.post(url, data = myData.encode(encoding="utf-8"), headers = myHeaders)
        #rsp = str(rsp).decode()
        #rsp = str(rsp)
        print(type(rsp))
        print(rsp)
    except Exception as e:
        print(e)
        print('{0}is not available'.format(url))
    continue
print('Finished')
