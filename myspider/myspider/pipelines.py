# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class MyspiderPipeline:
    # def process_item(self,item,spider):
    #     print(item)
    #     return item
    def __init__(self):
        self.data = []

    def process_item(self, item, spider):
        print(item)
        tmp = {}
        tmp['img'] = None
        tmp['prompt'] = item['que']
        tmp['label'] = item['ans']
        # print("tmp:\n")
        # print(tmp)
        self.data.append(tmp)

    def close_spider(self, spider):
        df = pd.DataFrame(self.data)
        df.to_json("agronet_data1.json", orient="records", force_ascii=False, indent=4)
        print('data saved successfully')