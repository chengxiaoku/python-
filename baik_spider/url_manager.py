#url管理器

class UrlManager(object):
    def __init__(self):
        #待爬取的url
        self.new_urls = set()
        #爬取过的url
        self.old_urls = set()

    #添加新的url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #批量添加url
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #判断是否有新的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #获取新的待爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()   #获取列表中的一个url 并且删除
        self.old_urls.add(new_url)
        return new_url
