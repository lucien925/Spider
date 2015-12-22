class HtmlOutputer(object):
    def __init__(self):
        self.data = []
    def collect_data(self, data):
        if data != None:
            self.data.append(data)
    def output_html(self):
        with open('output.html', 'w') as fp:
            fp.write('<html><body><table>')
            for data in self.data:
                fp.write('<tr>')
                fp.write('<td>%s</td><td>%s</td><td>%s</td>' % (data['url'], data['title'].encode('utf-8'), data['data'].encode('utf-8')))
                fp.write('</tr>')
            fp.write('</table></body></html>')
            fp.close()
