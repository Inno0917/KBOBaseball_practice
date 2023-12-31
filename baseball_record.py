import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import bs4
import requests
from selenium.webdriver.common.by import By
from tqdm import tqdm

options = webdriver.ChromeOptions()

def crawaling_get_driver(url, is_headless):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless') #창이 없이 크롬이 실행이 되도록 만든다
    options.add_argument("--start-fullscreen")  # 창이 최대화 되도록 열리게 한다.
    options.add_argument("disable-infobars")  # 안내바가 없이 열리게 한다.
    options.add_argument('--disable-dev-shm-usage')  # 공유메모리를 사용하지 않는다
    options.add_argument("disable-gpu")  # 크롤링 실행시 GPU를 사용하지 않게 한다.
    options.add_argument("--disable-extensions")  # 확장팩을 사용하지 않는다.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # 사이트에 접근하기 위해 get메소드에 이동할 URL을 입력한다.
    driver.get(url)

    return driver


def baseball_data_batter_record(driver):
    baseball_data = []
    for category in category_list:
        url = URL.format(category=category)
        driver.get(url)
        driver.maximize_window()

        year_list = [x.strip() for x in driver.find_element(By.CLASS_NAME,'select03').text.split('\n') if len(x) > 1]

        category_data_list = []
        for year in tqdm(year_list[:40]):
            driver.find_element(By.CLASS_NAME,'select03').click()
            xpath_format = '//option[@value="{year}"]'
            driver.find_element(By.XPATH,xpath_format.format(year = year)).click()

            time.sleep(1)

            temp_list = [x.split(' ') for x in driver.find_element(By.TAG_NAME, 'table').text.split('\n')]
            temp_data = pd.DataFrame(columns=temp_list[0])
            # print(temp_data)
            for i,temp in enumerate(temp_list[1:]):
                try:
                    temp_data.loc[i] = temp
                    time.sleep(1)
                except:
                    ip_index = temp_list[0].index('IP')
                    ip = temp[ip_index]
                    del temp[13]
                    temp[13] = ip + ' '+temp[13]
                    temp_data.loc[i] = temp
                    time.sleep(1)
            temp_data['Year'] = year
            category_data_list.append(temp_data)
            # print(category_data_list)
            time.sleep(1)
        category_data = pd.concat(category_data_list)
        baseball_data = category_data.to_csv("./KBOBaseball_batter.csv")


    return baseball_data

def baseball_data_pitcher_record(driver):
    baseball_data = []
    for category in category_list2:
        url = URL.format(category=category)
        driver.get(url)
        # driver.maximize_window()

        year_list = [x.strip() for x in driver.find_element(By.CLASS_NAME, 'select03').text.split('\n') if len(x) > 1]

        category_data_list = []
        for year in tqdm(year_list[:40]):
            driver.find_element(By.CLASS_NAME, 'select03').click()
            xpath_format = '//option[@value="{year}"]'
            driver.find_element(By.XPATH, xpath_format.format(year=year)).click()

            time.sleep(1)

            temp_list = [x.split(' ') for x in driver.find_element(By.TAG_NAME, 'table').text.split('\n')]
            temp_data = pd.DataFrame(columns=temp_list[0])

            for i, temp in enumerate(temp_list[1:]):
                try:
                    temp_data.loc[i] = temp
                    time.sleep(1)
                except:
                    ip_index = temp_list[0].index('IP')
                    ip = temp[ip_index]
                    del temp[13]
                    temp[13] = ip + ' ' + temp[13]
                    temp_data.loc[i] = temp
                    time.sleep(1)
            temp_data['Year'] = year
            category_data_list.append(temp_data)
            time.sleep(1)
        category_data = pd.concat(category_data_list)
        baseball_data = category_data.to_csv("./KBOBaseball_pitcher.csv")
    return baseball_data

def baseball_data_defance_record(driver):
    baseball_data = []
    for category in category_list3:
        url = URL.format(category=category)
        driver.get(url)
        # driver.maximize_window()

        year_list = [x.strip() for x in driver.find_element(By.CLASS_NAME, 'select03').text.split('\n') if len(x) > 1]

        category_data_list = []
        for year in tqdm(year_list[:21]):
            driver.find_element(By.CLASS_NAME, 'select03').click()
            xpath_format = '//option[@value="{year}"]'
            driver.find_element(By.XPATH, xpath_format.format(year=year)).click()

            time.sleep(1)

            temp_list = [x.split(' ') for x in driver.find_element(By.TAG_NAME, 'table').text.split('\n')]
            temp_data = pd.DataFrame(columns=temp_list[0])

            for i, temp in enumerate(temp_list[1:]):
                try:
                    temp_data.loc[i] = temp
                    time.sleep(1)
                except:
                    ip_index = temp_list[0].index('IP')
                    ip = temp[ip_index]
                    del temp[13]
                    temp[13] = ip + ' ' + temp[13]
                    temp_data.loc[i] = temp
                    time.sleep(1)
            temp_data['Year'] = year
            category_data_list.append(temp_data)
            time.sleep(1)
        category_data = pd.concat(category_data_list)
        baseball_data = category_data.to_csv("./KBOBaseball_defance.csv")
    return baseball_data

def baseball_data_runner_record(driver):
    baseball_data = []
    for category in category_list4:
        url = URL.format(category=category)
        driver.get(url)
        # driver.maximize_window()

        year_list = [x.strip() for x in driver.find_element(By.CLASS_NAME, 'select03').text.split('\n') if len(x) > 1]

        category_data_list = []
        for year in tqdm(year_list[:21]):
            driver.find_element(By.CLASS_NAME, 'select03').click()
            xpath_format = '//option[@value="{year}"]'
            driver.find_element(By.XPATH, xpath_format.format(year=year)).click()

            time.sleep(1)

            temp_list = [x.split(' ') for x in driver.find_element(By.TAG_NAME, 'table').text.split('\n')]
            temp_data = pd.DataFrame(columns=temp_list[0])

            for i, temp in enumerate(temp_list[1:]):
                try:
                    temp_data.loc[i] = temp
                    time.sleep(1)
                except:
                    ip_index = temp_list[0].index('IP')
                    ip = temp[ip_index]
                    del temp[13]
                    temp[13] = ip + ' ' + temp[13]
                    temp_data.loc[i] = temp
                    time.sleep(1)
            temp_data['Year'] = year
            category_data_list.append(temp_data)
            time.sleep(1)
        category_data = pd.concat(category_data_list)
        baseball_data = category_data.to_csv("./KBOBaseball_runner.csv")
    return baseball_data

URL = 'https://www.koreabaseball.com/Record/Player/{category}'
# URL2 = 'https://www.koreabaseball.com/Record/Player/{category}'
# URL3 = 'https://www.koreabaseball.com/Record/Player/{category}'
# URL4 = 'https://www.koreabaseball.com/Record/Player/{category}'

category_list = ['HitterBasic/Basic1.aspx']
category_list2 = ['PitcherBasic/Basic1.aspx']
category_list3 = ['Defense/Basic.aspx']
category_list4 = ['Runner/Basic.aspx']

driver1 = crawaling_get_driver(URL, True)
driver2 = crawaling_get_driver(URL, True)
driver3 = crawaling_get_driver(URL, True)
driver4 = crawaling_get_driver(URL, True)

batter_list = baseball_data_batter_record(driver1)
pitcher_list = baseball_data_pitcher_record (driver2)
defance_list = baseball_data_defance_record (driver3)
runner_list = baseball_data_runner_record (driver4)







