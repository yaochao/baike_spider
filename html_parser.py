# encoding: utf-8

from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):

    def _get_new_urls(self, url, soup):
        new_full_urls = set()
        a_nodes = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for a_node in a_nodes:
            new_url = a_node['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_full_urls.add(new_full_url)
        return new_full_urls

    def _get_new_data(self, url, soup):
        new_data = {}
        new_data['url'] = url
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        title = title_node.get_text()
        new_data['title'] = title
        summary_node = soup.find('div', class_='lemma-summary')
        summary = summary_node.get_text()
        new_data['summary'] = summary
        return new_data



        return new_data

    def parse(self, url, content):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data