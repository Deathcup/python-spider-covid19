import selenium
import requests as re
import regex
import time
import json

def getTimestamp():
    return int(time.time()*100)

url = 'https://vp.fact.qq.com/searchresult'
num = 400
callback = 'jsonp{}'.format(43)
params = {
    'title': '新冠',
    'num': num,
    # '_': getTimestamp(),
    'callback': callback
}

resp = re.get(url, params=params)
respcontent = resp.content.decode(encoding=resp.encoding)

pattern = 'jsonp[0-9]+\((.+)\)'
respjsonstr = regex.match(pattern, respcontent)[1]
respjson = json.loads(respjsonstr)
# print(respjson)
# with open("./output.json", 'w', encoding='utf8') as f:
#     f.write(respjsonstr)
# respjson = json.loads(respcontent)
print(len(respjson['content']))