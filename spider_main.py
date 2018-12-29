# encoding: utf-8

import url_manager, html_downloader, html_parser, html_outputer, exception_handler

class SpiderMain(object):

    def __init__(self):
        self.urlmanager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.exceptionchandler = exception_handler.ExceptionHandler()

    def crawl(self, root_url):
        count = 1
        self.urlmanager.add_new_url(root_url)
        while self.urlmanager.has_new_url():
            try:
                new_url = self.urlmanager.get_new_url()
                print 'crawl %d : %s' % (count, new_url)
                content = self.downloader.get_content(new_url)
                new_urls, new_data = self.parser.parse(new_url, content)
                self.urlmanager.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 10:
                    self.exceptionchandler.save_to_file()
                    print 'count %d complete' % count
                    break
                count = count + 1
            except Exception, e:
                self.exceptionchandler.url_collection(new_url)
                print 'crawl faild'
                print e

        self.outputer.output()


# main
if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)