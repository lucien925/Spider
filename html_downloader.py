from urllib import request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        with request.urlopen(url) as f:
            if f.status == 200:
                return f.read()
                
