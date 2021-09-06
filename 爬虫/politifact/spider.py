import request as re
import json
from bs4 import BeautifulSoup


# with open("./output.json", 'w', encoding='utf8') as f:
#     f.write(str(respcontent, encoding = "utf-8"))

with open("./titles.txt", 'w', encoding='utf8') as f:
    for num in range(1,28):     
        url = 'https://www.politifact.com/factchecks/list/?'

        params = {
            'page': num,
            'category': 'coronavirus',
        }

        resp = re.get(url, params=params)
        respcontent =resp.content

        soup = BeautifulSoup(respcontent)
        soup1 = soup.find_all('div',class_="m-statement__quote")

        for sentence in soup1:
            sentence = sentence.find('a')
            print(sentence.get_text())
            f.write(sentence.get_text())

#print(resp.content)