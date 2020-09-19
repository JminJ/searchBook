from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re
import math

bookName = '인간문제'

url = 'https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query={bookName}' #driver를 통해 접속할 사이트 주소

def search_book(url):
    driver = webdriver.Chrome('D:\Minju_project\chromedriver.exe') #웹 드라이버의 위치
    driver.get(url)

    try:
        element = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'txt_block')))
        book_list = []
        pageNum = re.findall('\d+',driver.find_element_by_xpath("//div[@id='content']/div[@class = 'tit_area']/span[@class='num num2']/strong").text)
        print(pageNum)
        pageNum = final_pageNum(int(pageNum[0]))
        print(type(pageNum))
    except TimeoutException:    # 예외 처리
        print('해당 페이지에 책 정보가 존재하지 않습니다.')
    
    print(pageNum)
   
def final_pageNum(pageNum):
    return math.ceil(pageNum / 20) # 받아온 총 책 정보를 한 페이지에 보여지는 양으로 니눠 페이지 수를 계산


search_book(url)




