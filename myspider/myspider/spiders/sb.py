import scrapy
from scrapy import Selector, Request
from ..items import MyspiderItem

class sb(scrapy.Spider):
    name = "sb"
    start_urls = []
    # start_urls=['http://www.agronet.com.cn/answer/detail/3309']
    for i in range(1,4150):
        start_urls.append('http://www.agronet.com.cn/answer/detail/' + str(i) )
    def parse(self, response):

        # 使用 XPath 表达式来定位和提取数据
        #使用text
        print(response.url)

        que = response.xpath("//span[@class='mxn_problem_h1']/text()").extract_first()
        ans = response.xpath("//div[@class='mxn_wyhd']/text()").extract_first()
        caina_ans = response.xpath("//div[@class='mxn_da_detail']/text()").extract_first()

        # 上面的是要搜索的，想还是直接用完整的xpath更省时间
        # que = response.xpath("/html/body/div[3]/div[@class='wid']/div[@class='mxnlist_layer1']/div[@class='mxnlist_left']/div[@class='iproblem mxn_10']/span[@class='mxn_problem_h1']/text()").extract_first()
        # ans = response.xpath("/html/body/div[3]/div[@class='wid']/div[@class='mxnlist_layer1']/div[@class='mxnlist_left']/div[@class='mxn_da mxn_10']/dl[@class='mxn_da_dl']/dt/div[@class='mxn_wyhd']/text()").extract_first()
        # caina_ans = response.xpath("/html/body/div[3]/div[@class='wid']/div[@class='mxnlist_layer1']/div[@class='mxnlist_left']/div[@class='mxn_da mxn_10']/div[@class='mxn_da_detail']/text()").extract_first()

        if caina_ans != None:
            ans = caina_ans
            # 优先选择采纳回答

        if ans == None or que == None:
            return

        #使用string
        # que = response.xpath("string(//span[@class='mxn_problem_h1'])").extract_first()
        # ans = response.xpath("string(//div[@class='mxn_wyhd']/text())").extract_first()
        # ans = ans.replace(' ', '')
        # ans = ans.replace('\n', ' ')
        # ans = ans.replace('\r', '')
        # que = que.replace(' ', '')
        # que = que.replace('\n', ' ')
        # que = que.replace('\r', '')

        # 处理一下格式，替换特定字符
        ans = ans.strip()  # 去除首尾的空白字符和换行符
        que = que.strip()
        que = que.replace('\u3000', ' ')# 替换u3000为空格
        ans = ans.replace('\u3000', ' ')
        ans = ans.replace('\r', '')# 去除\r保留\n
        que = que.replace('\r', '')
        # ans = " ".join(ans.split())  # 合并连续的空白字符为一个空格

        items = MyspiderItem(que=que, ans=ans)

        if ans!=None and que!=None:
            yield items