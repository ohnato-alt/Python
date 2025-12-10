

# import requests
# import xml.etree.ElementTree as ET


# address= "https://www.daum.net/"
# fname = address[address.rfind("/") + 1:]

# res = requests.get(address)
# if (res.status_code // 100) == 2:
#     with open("C:\\Users\\Admin\\MBCA\\"+fname, "bw") as fwrite:
#         fwrite.write(res.content)


# 웹 스크래핑 : 웹 페이지에서 특정 정보를 추출하는 작업

# 외부 모듈 : requests, beautifulsoup4 [별도 설치 필요]

# 웹 페이지를 분석 - 웹 페이지를 만드는 문법 HTML, CSS, JavaScript

# 아주 간단한 웹페이지를 만들어보기. [ HTML, CSS, JavaScript 언어를 다뤄보기. (web-test)]
import keyboard
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# response= requests.get('https://2017mrhi.github.io/web-test/')
# # print(response.text)
# # print()

# soup = BeautifulSoup(response.text, "html.parser")
# p_list = soup.select("H2")
# print(p_list)

# img = soup.select_one("#kk")
# print(img)

# response = requests.get('https://finance.naver.com/sise/')
# if response.status_code // 100 == 2 :
#     soup = BeautifulSoup(response.text, "html.parser")
#     p_list = soup.select("#KOSPI_now")
#     if len(p_list) > 0 :
#         print(p_list[0].text)q

# print(p_list)

driver = webdriver.Chrome()
driver.get("https://www.naver.com/")
# search_input = driver.find_element(By.CLASS_NAME, "search_input")

# search_input.send_keys("공원")
# search_button = driver.find_element(By.ID, "search-btn")
# search_button.click()
# print(driver.current_url)
# search_input = search_input.find_element(By.CLASS_NAME, "sds-comps-vertical-layout sds-comps-full-layout fds-news-item-list-desk")
# print(search_input)


search_button = driver.find_element(By.CLASS_NAME, "link_service")
main_window_handle = driver.current_window_handle
search_button.click()
print(driver.current_url)
all_window_handles = driver.window_handles

# 새로 열린 창의 핸들 찾기
for handle in all_window_handles:
    if handle != main_window_handle:
        new_window_handle = handle
        break

# 새로 열린 창으로 포커스 전환
driver.switch_to.window(new_window_handle)

# 새 창의 URL 가져오기
new_window_url = driver.current_url
print(f"새 창 URL: {new_window_url}")

keyboard.wait('ctrl+shift+x')





