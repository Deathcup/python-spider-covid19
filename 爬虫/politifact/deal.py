def gettext():
    txt = open("titles.txt","r",errors='ignore').read()
    txt = txt.lower()
    for ch in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~‘’':
        txt = txt.replace(ch,"")
    return txt

txt = gettext()
words = txt.split()
counts = {}

for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

print(items)
