# encoding: utf-8

import requests

class HtmlDownloader(object):

    def get_content(self, url):
        if url is None:
            return
        headers = {
            'Referer': 'https://baike.baidu.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return
        return response.content