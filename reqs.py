import requests
import time

i=0
f3=open("index.html","w")
f3.write("<!DOCTYPE html><html><head><title>Chargedup API for MAPS</title></head><body>")
f3.close()
while True:
 headers={"User-Agent":"Dalvik/2.1.0 (Linux; U; Android 8.0.0; Google Pixel Build/OPR6.170623.017)"}
 req=requests.get("https://play.googleapis.com/play/log/timestamp",headers=headers)
 res=req.text
 print res
 headers={"x-api-key":"a73644c1-c3f6-4f75-bfc9-59c28808bc36","Content-Type":"application/json","Authorization":"Bearer 3f2f0eb0-4c74-49c8-bfe6-4cfeee936dd7","User-Agent":"okhttp/4.3.1"}
 req=requests.get("https://api-v2.prod.chargedup.systems/stations?ts="+res,headers=headers)
 f=open(str(i)+"-hour-req.json",'w')
 f.write(str(req.json()))
 f.close()
 f1=open("index.html",'a')
 f1.write("</br><a href='"+str(i)+"-hour-req.json'>link to "+str(i)+" hour request</a>")
 f1.close()
 i+=1
 time.sleep(3600)