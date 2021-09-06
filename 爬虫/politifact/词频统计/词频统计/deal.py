import pandas as pd

def gettext():
    txt = open("titles.txt","r",encoding="utf-8").read()
    txt = txt.lower()
    for ch in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’0123456789%“”':
        txt = txt.replace(ch,"")
    return txt
txt = gettext()
words = txt.split()
# with open('result.txt','w',encoding = 'utf-8') as f:
#     for word in words:
#         f.write(word)

counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

data=[]
for item in items:
    data.append([item[0],item[1]])

pd = pd.DataFrame(data,columns=["word",'count'])
pd.to_csv("result.csv")
pd.to_excel("result.xlsx")
print(pd)
