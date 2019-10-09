# -*- coding:utf-8 -*-

from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe', chrome_options=chrome_options)
# driver.get("https://www.baidu.com")
# print(driver.page_source)
# driver.close()
#
# driver = webdriver.PhantomJS()
driver.get('https://wenku.baidu.com/view/1223b5f2a1116c175f0e7cd184254b35effd1a29.html')
html = driver.page_source
infos = etree.HTML(html).xpath('//div[@class="ie-fix"]')
for info in infos:
    data = info.xpath('./p/text()|./p/img/@src')
    for dat in data:
        dada = dat.replace('\xa0', '')
        if dada is None:
            pass
        else:
            print(dada, end='')
