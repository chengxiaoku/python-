#html 下载器
import urllib.request as myurllib

class HtmlDownloader:

    #下载url
    def download(self,url):
        if url is None:
            return  None
        #如果下载的网页比较复杂在这里修改代码
        response = myurllib.urlopen(url)
        if response.getcode() != 200:
            return None
        buf = response.read()
        buf = buf.decode('utf-8')
        return buf

