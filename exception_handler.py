# encoding: utf-8

class ExceptionHandler(object):

    def __init__(self):
        self.exception_urls = list()

    def url_collection(self, url):
        if url is None:
            return
        self.exception_urls.append(url)

    def save_to_file(self):
        if len(self.exception_urls) == 0:
            return
        f_cursor = open('exception_urls.txt', 'a')
        f_cursor.writelines([url + '\n' for url in self.exception_urls])
        f_cursor.close()