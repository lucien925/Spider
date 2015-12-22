class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    def add_new_url(self, url):
        if url is not None:
            self.new_urls.add(url)
    def add_new_urls(self, urls):
        if urls is not None and len(urls) != 0:
            for url in urls:
                self.new_urls.add(url)
    def get_new_url(self):
        get_url = self.new_urls.pop()
        self.old_urls.add(get_url)
        return get_url
    def has_new_url(self):
        return len(self.new_urls) != 0
