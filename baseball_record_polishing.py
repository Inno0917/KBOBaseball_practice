import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import pandas as pd
import bs4
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

def crawaling_get_driver(url):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    driver.maximize_window()
    return driver
def baseball_player_data_column(driver):
    bsObj = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    bsObjSelect = bsObj.find('select', {'name':'ctl00$ctl00$ctl00$cphContents$cphContents$cphContents$ddlSeason$ddlSeason'}).find_all('option')
    temp_all_list = []

    for key1, value1 in enumerate(bsObjSelect):
        # skip the 전체
        if key1 == len(bsObjSelect) - 1:
            continue
        selectBtn = Select(
            driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ddlSeason_ddlSeason"]'))
        selectBtn.select_by_visible_text(value1.get_text())
        time.sleep(1)
        # print(key, value)
        bsObjStatus = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        bsObjTr1 = bsObjStatus.find('table', {'class': 'tData01 tt'}).thead.find_all('tr')

        for key_tr, value_tr in enumerate(bsObjTr1):
            bsObjTh = value_tr.find_all('th')
            temp_list_head = []
            temp_list_head.append(value1.get_text())
            for key_td, value_td in enumerate(bsObjTh):
                resultText_th = value_td.get_text().replace(' ', '').strip()
                temp_list_head.append(resultText_th)
            temp_all_list.append(temp_list_head)
        break
    return temp_all_list
def baseball_player_data(driver):
    bsObj = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    bsObjSelect = bsObj.find('select', {'name':'ctl00$ctl00$ctl00$cphContents$cphContents$cphContents$ddlSeason$ddlSeason'}).find_all('option')
    player_list = []

    for key, value in enumerate(bsObjSelect):
        #skip the 전체
        if key == len(bsObjSelect) - 1:
            continue
        selectBtn = Select(driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ddlSeason_ddlSeason"]'))
        selectBtn.select_by_visible_text(value.get_text())
        time.sleep(1)
        # print(key, value)
        bsObjStatus = bs4.BeautifulSoup(driver.page_source, 'html.parser')

        bsObjTr2 = bsObjStatus.find('table', {'class': 'tData01 tt'}).tbody.find_all('tr')

        for key_tr, value_tr in enumerate(bsObjTr2):
            bsObjTd = value_tr.find_all('td')
            temp_list = []
            temp_list.append(value.get_text())
            for key_td, value_td in enumerate(bsObjTd):
                resultText_td = value_td.get_text().replace(' ', '').strip()
                temp_list.append(resultText_td)
            player_list.append(temp_list)
            print(temp_list)
    print("---Result Total :", len(player_list))
    print(player_list)
    player_list = baseball_player_data_column(driver) + player_list
    return player_list


def baseball_player_data_page_moving(driver, start, end):
        baseball_player_data_list_total = []

        for page in range(start, end):
            if page is None:
                try:
                    continue
                except:
                    baseball_player_data_list_total = baseball_player_data_column(driver) + baseball_player_data(driver)
                    driver.find_element(By.XPATH,
                                        '//*[@id="cphContents_cphContents_cphContents_ucPager_btnNo{}"]'.format(
                                            str(page))).click()
                    time.sleep(1)

        return baseball_player_data_list_total


def baseball_team_data_column(driver):
    bsObj = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    bsObjSelect = bsObj.find('select', {'name':'ctl00$ctl00$ctl00$cphContents$cphContents$cphContents$ddlSeason$ddlSeason'}).find_all('option')
    temp_all_list = []

    for key1, value1 in enumerate(bsObjSelect):
        # skip the 전체
        if key1 == len(bsObjSelect) - 1:
            continue
        selectBtn = Select(
            driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ddlSeason_ddlSeason"]'))
        selectBtn.select_by_visible_text(value1.get_text())
        time.sleep(1)
        # print(key, value)
        bsObjStatus = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        bsObjTr3 = bsObjStatus.find('table', {'class': 'tData tt'}).thead.find_all('tr')

        for key_tr, value_tr in enumerate(bsObjTr3):
            bsObjTh = value_tr.find_all('th')
            temp_list_head = []
            temp_list_head.append(value1.get_text())
            for key_td, value_td in enumerate(bsObjTh):
                resultText_th = value_td.get_text().replace(' ', '').strip()
                temp_list_head.append(resultText_th)
            temp_all_list.append(temp_list_head)
        break
    return temp_all_list

def baseball_team_data(driver):
    bsObj = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    bsObjSelect = bsObj.find('select', {'name':'ctl00$ctl00$ctl00$cphContents$cphContents$cphContents$ddlSeason$ddlSeason'}).find_all('option')
    team_data_list = []
    for key, value in enumerate(bsObjSelect):
        #skip the 전체
        if key == len(bsObjSelect) - 1:
            continue
        selectBtn = Select(driver.find_element(By.XPATH, '//*[@id="cphContents_cphContents_cphContents_ddlSeason_ddlSeason"]'))
        selectBtn.select_by_visible_text(value.get_text())
        time.sleep(1)

        bsObjStatus = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        bsObjTr4 = bsObjStatus.find('table', {'class':'tData tt'}).tbody.find_all('tr')

        for key_tr, value_tr in enumerate(bsObjTr4):
            bsObjTd_team = value_tr.find_all('td')
            temp_list = []
            temp_list.append(value.get_text())
            for key_td, value_td in enumerate(bsObjTd_team):
                resultText_td_team = value_td.get_text().replace(' ', '').strip()
                temp_list.append(resultText_td_team)
            team_data_list.append(temp_list)
            print(temp_list)
    print("---Result Total :", len(team_data_list))
    print(team_data_list)
    team_data_list = baseball_team_data_column(driver) + team_data_list
    return team_data_list

def baseball_team_data_page_moving(driver, start, end):
        baseball_team_data_list_total = []

        for page in range(start, end):
            if page is not None:
                try:
                    bsObj = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                    bsObj.find_element(By.XPATH,
                                        '//*[@id="cphContents_cphContents_cphContents_ucPager_btnNo{}"]'.format(
                                            str(page))).click()
                    baseball_team_data_list_total = baseball_team_data_column(driver) + baseball_team_data(driver)

                    time.sleep(1)

                except:
                    continue


        return baseball_team_data_list_total





URL1 = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'
driver1 = crawaling_get_driver(URL1)
time.sleep(1)
batter_list = baseball_player_data(driver1)
pdList_Batter = pd.DataFrame(batter_list)
pdList_Batter.to_csv("./KBO_Batter_Record_Test.csv", encoding='CP949', index='True')
time.sleep(1)
driver1.close()

URL2 = 'https://www.koreabaseball.com/Record/Player/PitcherBasic/Basic1.aspx'
driver2 = crawaling_get_driver(URL2)
time.sleep(1)
pitcher_list = baseball_player_data(driver2)
pdList_pitcher = pd.DataFrame(pitcher_list)
pdList_pitcher.to_csv("./KBO_Pitcher_Record.csv", encoding='CP949', index = 'True')
time.sleep(1)
driver2.close()

URL3 = 'https://www.koreabaseball.com/Record/Player/Defense/Basic.aspx'
driver3 = crawaling_get_driver(URL3)
time.sleep(1)
defence_list = baseball_player_data(driver3)
pdList_defence = pd.DataFrame(defence_list)
pdList_defence.to_csv("./KBO_Defence_Record.csv", encoding='CP949', index = 'True')
time.sleep(1)
driver3.close()

URL4 = 'https://www.koreabaseball.com/Record/Player/Runner/Basic.aspx'
driver4 = crawaling_get_driver(URL4)
time.sleep(1)
runner_list = baseball_player_data(driver4)
pdList_runner = pd.DataFrame(runner_list)
pdList_runner.to_csv("./KBO_Runner_Record.csv", encoding='CP949', index = 'True')
time.sleep(1)
driver4.close()

URL5 = 'https://www.koreabaseball.com/Record/Team/Hitter/Basic1.aspx'
driver5 = crawaling_get_driver(URL5)
time.sleep(1)
team_Hitting_list = baseball_team_data(driver5)
pdList_team_Hitting = pd.DataFrame(team_Hitting_list)
pdList_team_Hitting.to_csv("./KBO_Team_Hitting_Record.csv", encoding='CP949', index='True')
time.sleep(1)
driver5.close()

URL6 = 'https://www.koreabaseball.com/Record/Team/Pitcher/Basic1.aspx'
driver6 = crawaling_get_driver(URL6)
time.sleep(1)
team_pitcher_list = baseball_team_data(driver6)
pdList_team_pitcher = pd.DataFrame(team_pitcher_list)
pdList_team_pitcher.to_csv("./KBO_Team_Pitcher_Record.csv", encoding='CP949', index = 'True')
time.sleep(1)
driver6.close()

URL7 = 'https://www.koreabaseball.com/Record/Team/Defense/Basic.aspx'
driver7 = crawaling_get_driver(URL7)
time.sleep(1)
team_defence_list = baseball_team_data(driver7)
pdList_team_defence = pd.DataFrame(team_defence_list)
pdList_team_defence.to_csv("./KBO_Team_Defence_Record.csv", encoding='CP949', index = 'True')
time.sleep(1)
driver7.close()

URL8 = 'https://www.koreabaseball.com/Record/Team/Runner/Basic.aspx'
driver8 = crawaling_get_driver(URL8)
time.sleep(1)
team_runner_list = baseball_team_data(driver8)
pdList_team_runner = pd.DataFrame(team_runner_list)
pdList_team_runner.to_csv("./KBO_Team_Runner_Record.csv", encoding='CP949', index = 'True')
time.sleep(1)
driver8.close()

# column1 = id,year,ranking,name,team_name,AVG(타율),G(경기),PA(타석),AB(타수),R(득점),H(안타),2B(2루타),3B(3루타),HR(홈런),TB(루타),RBI(타점),SAC(희생번트),SF(희생플라이)
# column2 = id,year,ranking,name,team_name,ERA(평균자책점),G(경기),W(승리),L(패배),SV(세이브),HLD(홀드),WPCT(승률),IP(이닝),H(피안타),HR(피홈런),BB(볼넷),HBP(사구),SO(삼진),R(실점),ER(자책점),WHIP(이닝당 출루허용률)
# column3 = id,year,ranking,name,team_name,POS(포지션),G(경기),GS(선발경기),IP(수비이닝),E(실책),PKO(견제사),PO(자살),A(보살),DP(병살),FPCT(수비율),PB(포일),SB(도루허용),CS(도루실패),CS%(도루저지율)
# column4 = id,year,ranking,name,team_name,G(경기),SBA(도루시도),SB(도루성공),CS(도루실패),SB%(도루성공률),OOB(주루사),PKO(견제사)
# column5 = id,year,ranking,team_name,AVG(팀타율),G(경기수),PA(팀전체타석),AB(팀전체타수),R(득점),H(안타),2B(2루타),3B(3루타),HR(홈런),TB(루타),RBI(타점),SAC(희생번트),SF(희생플라이)
# column6 = id,year,ranking,team_name,ERA(평균자책점),G(경기),W(승리),L(패배),SV(세이브),HLD(홀드),WPCT(승률),IP(이닝),H(피안타),HR(홈런),BB(볼넷),HBP(사구),SO(삼진),R(실점),ER(자책점),WHIP(이닝당 출루허용율)
# column7 = id,year,ranking,team_name,G(경기),E(실책),PKO(견제사),PO(자살),A(보살),DP(병살),FPCT(수비율),PB(포일),SB(도루허용),CS(도루실패),CS%(도루저지율)
# column8 = id,year,ranking,team_name,SBA(도루시도),SB(도루성공),CS(도루실패),SB%(도루성공율),OOB(주루사),PKO(견제사)