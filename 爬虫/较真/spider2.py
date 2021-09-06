import requests
import pandas as pd


class SpiderRumor(object):
    def __init__(self):
        self.url = "https://vp.fact.qq.com/loadmore?artnum=0&page=%s"
        self.header = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        }

    def spider_run(self):
        df_all = list()
        for url in [self.url % i for i in range(30)]:
            data_list = requests.get(url, headers=self.header).json()["content"]
            temp_data = [[df["title"], df["date"], df["result"], df["explain"], df["tag"]] for df in data_list]
            df_all.extend(temp_data)
            #print(temp_data[0])
        pd.DataFrame(df_all, columns=["title", "date", "result", "explain", "tag"]).to_csv("冠状病毒谣言数据2.csv", encoding="utf_8_sig")


if __name__ == '__main__':
    spider = SpiderRumor()
    spider.spider_run()
