#Made by Julián Flores
#01 avril 2019---CDMX
#robotfpv

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

# f = open("bot.log", "a")
message_text='test' # message you want to send
no_of_message=1 # no. of time you want the message to be send
moblie_no_list=[6282285807100] # list of phone number can be of any length

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def element_invisibility_located(by,xpath,time):
    element_present = EC.invisibility_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Firefox()
driver.get("http://web.whatsapp.com")
sleep(10) #wait time to scan the code in second

def get_display_name(phone_no):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to.alert.accept()
    except Exception as e:
        pass
    try:
        # element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        # txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        sleep(8)
        profile_picture_xpath = '/html/body/div[1]/div/div/div[4]/div/header/div[1]'
        element_presence(By.XPATH, profile_picture_xpath, 30)
        profile_picture = driver.find_element(By.XPATH, profile_picture_xpath)
        profile_picture.click()
        try:
            name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[2]/span/span')
            print("name: {} with phone no : {}".format(name.text, phone_no))
        except Exception as e:
            print("name: Unknown with phone no : {}".format(phone_no))
    except Exception as e:
        print("invalid phone no : {} with error: {}".format(str(phone_no), str(e)))

# for moblie_no in moblie_no_list:
#     try:
#         get_display_name(moblie_no)
#     except Exception as e:
#         sleep(10)
#         is_connected()


for x in range(0, 999):
    prefix = str(x).zfill(3)
    try:
        get_display_name('6282285807' + prefix)
        sleep(10)
    except Exception as e:
        sleep(10)
        is_connected()