# encoding: utf-8

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta charset="utf-8">')
        fout.write('<title>')
        fout.write('output')
        fout.write('</title>')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<table>')

        # python 默认编码 ascii,需要转换成 utf-8编码
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()