import crawler
if __name__ == "__main__":
    zhihu_crawler = crawler.Zhihu_crawler("https://www.zhihu.com/people/xu-zhi-75-83")
    zhihu_crawler.send_request()
    zhihu_crawler.print_data_out()