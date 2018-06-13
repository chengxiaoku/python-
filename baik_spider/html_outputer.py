#将数据写入到html页面中 在此显示

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    #收集数据
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    #写入 显示数据
    def output_html(self):
        fout = open("output.html","w")
        fout.write("<html><body><table>")
        for data in self.datas :
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode("utf-8"))
            fout.write("<td>%s</td>" % data['summary'].encode("utf-8"))
            fout.write("</tr>")
        fout.write("</table></body></html>")

        fout.close()