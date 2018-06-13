#爬虫主调程序
from baik_spider import url_manager,html_download,html_outputer,html_parser

class SpiderMain(object):
    def __init__(self):
        #url 管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_download.HtmlDownloader()
        #解析器
        self.parser = html_parser.HtmlParser()
        #输入器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        #标明当前url 是第几个
        count = 1
        self.urls.add_new_url(root_url)
        #url管理器有待爬取的url 时

        while self.urls.has_new_url():
            try:        #因为有可能爬取过程中url失效故要加入异常处理
                #获取待爬取的url
                new_url = self.urls.get_new_url()
                print("craw%d : %s"%(count,new_url))
                #启动下载器下载页面
                html_cont = self.downloader.download(new_url)
                #print(html_cont)
                #解析页面数据
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                #url 添加至url 管理器
                self.urls.add_new_urls(new_urls)
                #收集数据
                self.outputer.collect_data(new_data)
                #停止条件
                if count == 100:
                    break
                count = count + 1
            except:
                print("出现了点小问题")
         #输出收集好的数据
        self.outputer.output_html()

if __name__=="__main__":
    #设定爬虫的入口
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)