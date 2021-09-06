'''
python 爬虫  爬取腾讯较真查证平台，对新型冠状病毒“谣言”的新闻进行数据分析
http://www.cppcns.com/jiaoben/python/300617.html
Authon: taotao
Date:20200227
'''

import requests
import pandas


class SpiderRumor(object):
    def __init__(self):
        self.url = "https://vp.fact.qq.com/loadmore?artnum=0&page=%s"
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3269.3 Safari/537.36"
        }

    def Run_spider(self):
        df_all = list()
        for url in [self.url % i for i in range(40)]:
            data_list = requests.get(url, headers=self.header).json()["content"]
            print(data_list)
            tempdata = [[df["title"], df["date"], df["result"], df["explain"], df["tag"]] for df in data_list]
            # print(tempdata)
            df_all.extend(tempdata)

            # 生成Excel表
            pd = pandas.DataFrame(df_all, columns=["title", "date", "result", "explain", "tag"]).to_csv(
                "关于新冠状病毒的谣言统计表.csv", encoding="utf_8_sig")


# 程序过程

if __name__ == '__main__':
    spider = SpiderRumor()
    spider.Run_spider()