# encoding: utf-8

import requests

class HtmlDownloader(object):

    def get_content(self, url):
        if url is None:
            return
        response = requests.get(url)
        if response.status_code != 200:
            return
        return response.content
    