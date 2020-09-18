from selenium import webdriver
import time

url = 'https://book.naver.com/' #driver를 통해 접속할 사이트 주소

def search_book(bookName):
    driver = webdriver.Chrome('D:\Minju_project\chromedriver.exe') #웹 드라이버의 위치
    driver.get(url)

    assert "네이버 책" in driver.title
    elem = driver.find_element_by_id("nx_query") #네이버 책 사이트의 검색 창의 html id
    elem.send_keys(bookName)    
    
    elem = driver.find_element_by_id("search_btn") #네이버 책 사이트의 검색 버튼의 html id
    elem.click()

    time.sleep(10)
    driver.qiut()

search_book("데미안")

