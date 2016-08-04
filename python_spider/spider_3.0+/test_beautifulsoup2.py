from bs4 import BeautifulSoup
import os
import urllib.request
import urllib.parse
import urllib.error

#Author = Zane Time = 16/8/2 爬取图片链接

#爬取html文件
def open_url(url):

    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason)

    html = response.read()
    #print(html)
    return html

def get_link(url):
    html = open_url(url)
    soup = BeautifulSoup(html, 'html.parser')
    #定位
    divs = soup.select('div[class="postContent"]')
    print(divs)
    #图片集合
    img_urls = []
    print(divs)
    for div in divs:
        img_url = div.p.find('img')['src']
        print(img_url)
        img_urls.append(img_url)
    return img_urls

def save_img(folder, img_addresses):
    for address in img_addresses:
        addr = address.split('/')[6:8]
        addr_2 = addr[0] + addr[1] + '.jpg'
        print(addr)
        with open(addr_2, 'wb') as f:
            img = open_url(address)
            f.write(img)

def download_img(fold = 'mezi_pict'):
    urls = get_link("http://www.meizitu.com/")
    os.mkdir(fold)
    os.chdir(fold)
    save_img(fold, urls)

if __name__ == '__main__':
    download_img()



