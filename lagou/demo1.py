import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')

if __name__ == '__main__':
    htmlurl = 'https://www.lagou.com/jobs/list_PHP'
    print(getHtml(htmlurl))