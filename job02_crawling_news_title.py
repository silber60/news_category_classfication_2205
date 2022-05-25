from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time

pages = [110, 110, 110, 78, 110, 66]

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100#&date=%2000:00:00&page=1'

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)

for i in range(0, 6):
    titles = []
    for j in range(1,pages[i]+1):
        url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}#&date=%2000:00:00&page={}'.format(i, j)
        driver.get(url)
        time.sleep(2)
        for k in range(1, 5):
            for l in range(1, 6):
                x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt[2]/a'.format(k, l)
                title = driver.find_element_by_xpath(x_path).text
                print(title)












#//*[@id="section_body"]/ul[1]/li[1]/dl/dt[2]/a
#//*[@id="section_body"]/ul[1]/li[2]/dl/dt[2]/a
#//*[@id="section_body"]/ul[1]/li[3]/dl/dt[2]/a
#//*[@id="section_body"]/ul[1]/li[4]/dl/dt[2]/a
#//*[@id="section_body"]/ul[1]/li[5]/dl/dt[2]/a
#//*[@id="section_body"]/ul[2]/li[1]/dl/dt[2]/a
#//*[@id="section_body"]/ul[2]/li[2]/dl/dt[2]/a
#//*[@id="section_body"]/ul[3]/li[1]/dl/dt[2]/a
#//*[@id="section_body"]/ul[4]/li[5]/dl/dt[2]/a








