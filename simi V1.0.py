import time
import urllib.request
import base64


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

options = Options()
#options.add_argument('--headless')

value = "food"
#driver = webdriver.Chrome()
driver = uc.Chrome(options=options)

try:
    #open similarweb
    driver.get('https://www.similarweb.com/')
    time.sleep(3)
    
    #find the search bar element
    input = driver.find_element(By.XPATH,'//*[@id="hm-hero-search"]/div/div/form/input')
    #time.sleep(3)

    #To enter the search keyword
    input.send_keys(value)
    input.send_keys(Keys.ENTER)

    #result = driver.find_elements(By.CLASS_NAME,'search-results__card-body search-results__card-body--link')
    #print(result)

    # 定位并处理CAPTCHA
    #captcha_element = driver.find_element(By.ID,'recaptcha-anchor')
    #captcha_element.send_keys("true")
    
    time.sleep(1000000)



finally:
  
    driver.quit()

