import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import urllib
import pandas as pd
import bs4
from datetime import datetime
import requests
import os
import shutil
import sys
import json
import urllib.request
from selenium.webdriver.common.by import By
import re
from PIL import Image

options = webdriver.ChromeOptions()

date = str(datetime.today().month) + '월' + str(datetime.today().day) + '일'

def crawaling_get_driver(url, is_headless):
    options = webdriver.ChromeOptions()
    options.add_argument('headless') #창이 없이 크롬이 실행이 되도록 만든다
    options.add_argument("--start-fullscreen")  # 창이 최대화 되도록 열리게 한다.
    options.add_argument("disable-infobars")  # 안내바가 없이 열리게 한다.
    options.add_argument('--disable-dev-shm-usage')  # 공유메모리를 사용하지 않는다
    options.add_argument("disable-gpu")  # 크롤링 실행시 GPU를 사용하지 않게 한다.
    options.add_argument("--disable-extensions")  # 확장팩을 사용하지 않는다.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 사이트에 접근하기 위해 get메소드에 이동할 URL을 입력한다.
    driver.get(url)
    return driver




# 네이버 야구 특정 일자의 일정/ 결과 페이지로 이동하기
data_list = []
def naver_sports_baseball_record(url):
     driver = crawaling_get_driver(url,True)
     driver.find_element(By.CLASS_NAME, 'tab_team').find_element(By.LINK_TEXT, "키움").click()

     return driver

# 해당 일자 일정 / 결과 데이터 가져오기
def naver_sports_baseball_result(driver):
    bsObj = bs4.BeautifulSoup(driver.page_source, "html.parser")
    game = bsObj.find("div",{"class":"tb_wrap"}).find_all("div",{"class":re.compile("^sch_tb")})
    today = datetime.today().day
    global isDH

    if (game[today - 1].find("td", attrs = {"rowspan": "2"}) == None):  # 금일 더블 헤더 일정이 있는지 체크
         isDH = False
    else:
         isDH = True

    if not isDH:
        link = 'https://sports.news.naver.com/' + game[today-2].find("span", attrs = {"class": "td_btn"}).find("a")["href"]
        enterPage(link,0)
    else:
        for i in range(0, 2):
            link = 'https://sports.news.naver.com/' + \
                   game[today-2].find_all("span", attrs = {"class": "td_btn"})[i].find_all("a")[0]["href"]
            enterPage(link, i+1)
    return driver

def enterPage(link, num):

    driver.get(link)
    bsObj = bs4.BeautifulSoup(driver.page_source, "html.parser")
    bsObjList = bsObj.find_all("div",{"class":"Home_container__3HKK4"})
    print(bsObjList)
    contents_all = []
    for key, value in enumerate(bsObjList):

        contents_list = []

        date = value.find("p",{"class":"MatchBox_date__1bJ9G"}).get_text()

        time = value.find("span",{"class":"MatchBox_time__2z_nB"}).get_text()

        stadium = value.find("p",{"class":"MatchBox_stadium__17mQ4"}).get_text()


        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip"
        }

        contents_list.append(date)

        contents_list.append(time)

        contents_list.append(stadium)

        contents_all.append(contents_list)

    return contents_all



#     try :
#         time.sleep(1)
#         global isWin
#         # 홈 / 원정 확인
#         team = driver.find_elements(By.CLASS_NAME,'MatchBox_text__22e-R')[0].text
#         print(team)
#         result = driver.find_element(By.CLASS_NAME, "Home_game_head__3EEZZ").screenshot_as_png
#
#         recordGraph = driver.find_element(By.CLASS_NAME, "TeamVS_comp_team_vs__fpu3N").screenshot_as_png
#
#         if(team.find('키움') == -1 ):
#             playerRecord = driver.find_elements(By.CLASS_NAME, "PlayerRecord_tabpanel__3GYt9")[0].screenshot_as_png
#             print(playerRecord)
#             if(team.find("승") == -1):
#                 isWin = True
#             else:
#                 isWin = False
#         else :
#             playerRecord = driver.find_element(By.CLASS_NAME, "PlayerRecord_tabpanel__3GYt9")[1].screenshot_as_png
#
#             if(team.find("승")==-1):
#                 isWin = False
#             else:
#                 isWin = True
#         print(isWin)
#
#         createImage('result', result, num)
#         createImage('recordGraph', recordGraph, num)
#         createImage('playerRecord',playerRecord,num)
#     except:
#         print("Enter Page Error")
#
#
# def createImage(filename, file_png, num):
#     if not isDH:
#         with open('image/{}_{}.png'.format(filename,date), 'wb') as f:
#             f.write(file_png)
#     else:
#         with open('image/{}_{}_{}.png'.format(filename,date,num), 'wb') as f:
#             f.write(file_png)
#
#
# def createDirectory():
#     try:
#         if not os.path.exists('image'):
#             os.makedirs('image')
#     except:
#         print('createDirectory Error')
#
# def removeDirectory():
#     try:
#         if os.path.exists('image'):
#             shutil.rmtree('image')
#     except OSError:
#         print('removeDirectory Error')

url = "https://sports.news.naver.com/kbaseball/schedule/index"


driver = naver_sports_baseball_record(url)
time.sleep(1)
driver = naver_sports_baseball_result(driver)
time.sleep(1)

