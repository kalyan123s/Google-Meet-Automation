import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url="https://meet.google.com/bfr-wjaw-wat"

driverPath="D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

#this three lines are used for preventing automatically quit the chrome
browserOptions = webdriver.ChromeOptions()                                   
browserOptions.add_experimental_option('detach', True)                               
browserOptions.add_experimental_option('excludeSwitches', ['enable-logging'])   

#  By disabling this feature, we can avoid being detected as a bot and can access the website easily.
browserOptions.add_argument('--disable-blink-features=AutomationControlled')
# Below method will allow microphone and camera
browserOptions.add_experimental_option("prefs", {
 
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    # below code allow notifications from meet
    "profile.default_content_setting_values.notifications": 1
})
chromeService=Service(driverPath)
#service=chromeService specifies that we want to use the custom ChromeDriver service whose path is in driver path
#inside the bracket we have to necessarily give argument as browserOptions so that chrome don't quit automatically
browser=webdriver.Chrome(service=chromeService, options = browserOptions)    
browser.maximize_window()
browser.get(url)
time.sleep(1)

def sign_in():
    login_btn=browser.find_element(By.CSS_SELECTOR,"span[class='l4V7wb Fxmcue']")
    login_btn.click()
    
    browser.implicitly_wait(10)
    email_box=browser.find_element(By.CSS_SELECTOR, "input[type='email']")
    email_box.clear()
    email_box.send_keys('kalyansharma855@nitgoa.ac.in')
    next_btn=browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    next_btn.click()
    browser.implicitly_wait(10)
    
    time.sleep(2)
    # Danger! To find password_box use X_path not full x_path since its varrying with time that i dont know why?
    password_box = browser.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input")
    password_box.click()  # Click on the password field before typing
    pyautogui.write('')


    
    browser.implicitly_wait(10)
    again_next_btn=browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
    again_next_btn.click()
    

def off_camera_mic():
    mic=browser.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[20]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[1]/div/div/div[1]/span")
    browser.implicitly_wait(15)
    mic.click()
    
    time.sleep(1)
    camera=browser.find_element(By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[20]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[2]/div/div[1]/span/span/div/span[2]")
    browser.implicitly_wait(15)
    camera.click()
    time.sleep(1)
  
def ready_to_join():
    join_now=browser.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[20]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span")
    join_now.click()
  
  
# functions call  
sign_in()
off_camera_mic()
ready_to_join()
