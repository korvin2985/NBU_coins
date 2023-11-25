from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time



options = webdriver.ChromeOptions()
options.add_argument('lang=ru')
options.add_argument("start-maximized")

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#, options=options)
driver = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")
driver.implicitly_wait(1)
#driver.maximize_window()
width = 628
height = 1000
driver.set_window_size(width, height)
driver.get("https://coins.bank.gov.ua/")



class Locators():
    button_menu_cabinet_locator = (By.CLASS_NAME, "small-menu-cabinet")
    field_email_login_locator = (By.CLASS_NAME, "reg_input.form-control")
    field_psw_locator = (By.ID, "password")
    button_login_locator = (By.CLASS_NAME, "btn.btn-default")
    button_all_things_locator = (By.CSS_SELECTOR, "body > div.page-wrap > header > div.add_nav.bank_add_nav > nav > div > div.block_categories > div > ul > li:nth-child(1) > a > span")
    button_all_coins_locator = (By.CLASS_NAME, "show-sub_ul")
    button_three_lines_locator = (By.CLASS_NAME, "block_categories")
    button_add_to_basket_locator = (By.CLASS_NAME, "styled_svg.card-hov")
    button_select_coins_type_locator = (By.CSS_SELECTOR, "body > div.page-wrap > header > div.add_nav.bank_add_nav > nav > div > div.block_categories > div > ul > li:nth-child(2) > button")
    button_gold_coins_locator = (By.CSS_SELECTOR, "body > div.page-wrap > header > div.add_nav.bank_add_nav > nav > div > div.block_categories > div > ul > li:nth-child(2) > ul > li > div > div:nth-child(1) > div > a > span")
    weight_locator = (By.CLASS_NAME, "char-right")
    cost_locator = (By.ID, "summ_price")
    open_coin_locator = (By.CLASS_NAME, "p_img_href.not-slider")
    coin_name_locator = (By.CLASS_NAME, "model_product")
    left_row_locator = (By.CLASS_NAME, "char-left")


class List():
    wish_list = [
        "Богиня Апі",
        "Бджола",
        "Їжак",
        "Байбак",
        "Лелека",
        "Саламандра",
        "Риби",
        "Водолій",
        "Козеріг",
        "Близнюки",
        "Телець",
        "Овен",
        "Оранта"
    ]


# "Український балет",
# "Нестор-літописець",
# "1 Гривня",
# "10 років проголошення незалежності",
# "Хрещення Русі",
# "Різдво Христовe",
# "Успенський собор Києво-Печерської лаври",
# "Михайлівський Золотоверхий собор",
# "Енеїда",
# "Київський псалтир",


class BuyCoin():
    def login():
        button_menu_cabinet = driver.find_element(*Locators.button_menu_cabinet_locator)
        button_menu_cabinet.click()
        time.sleep(1)
        field_email_login = driver.find_element(*Locators.field_email_login_locator)
        field_email_login.send_keys("claudiajenrpm365@gmail.com")
        field_psw_locator = driver.find_element(*Locators.field_psw_locator)
        field_psw_locator.send_keys("29852985_Kk")
        button_login = driver.find_element(*Locators.button_login_locator)
        button_login.click()


    def find_coin():
        #button_three_lines = driver.find_element(*Locators.button_three_lines_locator)
        #button_three_lines.click()
        #button_all_things = driver.find_element(*Locators.button_all_things_locator)
        #button_all_things.click()
        #button_select_coins_type = driver.find_element(*Locators.button_select_coins_type_locator)
        #button_select_coins_type.click()
        #button_gold_coins = driver.find_element(*Locators.button_gold_coins_locator)
        #button_gold_coins.click()


        #driver.get("https://coins.bank.gov.ua/pam-atni-moneti/c-422.html")
        driver.get("https://coins.bank.gov.ua/zoloti-moneti/c-449.html")


    def add_to_basket(current_wish_list):
        new_list = current_wish_list
        Catalog_items = driver.find_elements(By.CLASS_NAME, 'p_description')
        wait = WebDriverWait(driver, 10)
        for i in Catalog_items:
            i1 = i.find_element(By.CLASS_NAME, 'model_product')
            if (i1.get_attribute('text') != None):
                txt = i1.get_attribute('text')
                for j in current_wish_list:
                    if j in txt:
                        try:
                            i2 = i.find_element(By.CLASS_NAME, "main-basked-icon.add2cart")

                            driver.execute_script("arguments[0].scrollIntoView();", i)
                            i2.click()
                            new_list.remove(j)
                            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'styled_svg.white_svg.card-ok')))
                            #ime.sleep(2)
                            # ref = i.get_attribute('href')
                            # driver.get(ref)
                            # catalog.append(txt)
                            #styled_svg white_svg card-ok
                        except:
                            h = 1
        return new_list


class grammCost():

    def create_list():
        gold_list = []
        gold_list_description = driver.find_elements(By.CLASS_NAME, 'p_description')
        coins_number = len(gold_list_description)
        for j in range(coins_number): #gold_list_description:

            time.sleep(0.5)
            #driver.switch_to.window(driver.window_handles[j])
            driver.get("https://coins.bank.gov.ua/zoloti-moneti/c-449.html")
            i = driver.find_elements(By.CLASS_NAME, 'p_description')[j]
            driver.execute_script("arguments[0].scrollIntoView();", i)
            coin_name = i.find_element(*Locators.coin_name_locator).get_attribute('text')
            button_open_coin = i.find_element(*Locators.open_coin_locator)
            button_open_coin.click()
            cost = driver.find_element(*Locators.cost_locator).text
            weight = driver.find_elements(*Locators.weight_locator)

            masa = driver.find_elements(*Locators.left_row_locator)
            masa_text = "Маса"
            nomer = 0
            for m in masa:
                if masa_text in m.text:
                    weight_opposite = weight[nomer].text
                    break
                nomer = nomer+1

            price = float(cost.replace('грн','').replace(' ','')) / float(weight_opposite.replace(',','.'))

            gold_list.append([coin_name, float(weight_opposite.replace(',','.')), float(cost.replace('грн','').replace(' ','')), price])

            #driver.execute_script("window.open('');")



        return gold_list





BuyCoin.login()
BuyCoin.find_coin()
coin_list = grammCost.create_list()
best_rate = sorted(coin_list, key=lambda x: x[3])
best_price = sorted(coin_list, key=lambda x: x[2])
print(best_rate)
print(best_price)










# count = 0
# BuyCoin.login()
# current_wish_list = List.wish_list
# while (count < 1200):
#     #print(count, current_wish_list)
#     try:
#         BuyCoin.find_coin()
#         current_wish_list = BuyCoin.add_to_basket(current_wish_list)
#         time.sleep(1)
#         count = count + 1
#     except:
#         time.sleep(1)





#https://coins.bank.gov.ua/catalog.html
#https://coins.bank.gov.ua/catalog.html?page=2&sort=catalog
#https://coins.bank.gov.ua/catalog.html?page=3&sort=catalog
#https://coins.bank.gov.ua/catalog.html?page=4&sort=catalog



#bank_price_name
#model_product
#main-basked-icon add2cart
#main-basked-icon gray







