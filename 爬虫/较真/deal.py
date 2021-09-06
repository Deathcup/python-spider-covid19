import pandas as pd
import jieba 

data = pd.read_csv("data.csv")


titles = data['title']
counts = {}
for title in titles:
    wordlist = jieba.cut(str(title))
    for word in wordlist:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0) + 1

counts=sorted(counts.items(),key=lambda x:x[1],reverse=True)

datas = []
for word in counts:
    datas.append([word[0],word[1]])

pd = pd.DataFrame(datas, columns=["word", "count"])
pd.to_csv("较真统计结果.csv")
pd.to_excel("较真统计结果.xlsx")
print(pd)