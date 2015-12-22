
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_link = urljoin(page_url, new_url)
            new_urls.add(new_full_link)
        return new_urls
    def _get_new_data(self, page_url, soup):
        new_data = {}
        summary_node = soup.find('div', class_='lemma-summary')
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title')
        new_data['summary'] = summary_node.get_text()
        new_data['title'] = title_node.get_text()
        new_data['url'] = page_url
        return new_data

    def parse(self, page_url, html_content):
        if page_url != None and html_content != None:
            soup = BeautifulSoup(html_content, 'html.parser', from_encoding="UTF-8")
            new_urls = self._get_new_urls(page_url, soup)
            new_data = self._get_new_data(page_url, soup)
            return new_urls, new_data
