#!/usr/bin/python3

import xmlrpc.client

#from Config.Config import *
#from Network.Http.Utils import Utils

Mac = "545454545454"
url = "http://119.28.67.228/xmlrpc.php"
#app = xmlrpc.client.ServerProxy(url, encoding="utf-8")
print(xmlrpc.client.ServerProxy.system.listMethods())
