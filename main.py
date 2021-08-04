from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

PATH = "C:/Development/chromedriver.exe"
TINDER = "https://tinder.com/"
MAIL = ""   #Your mail
PASS = "" #Your pass
driver = webdriver.Chrome(executable_path=PATH)

driver.get(TINDER)
time.sleep(20)
log = driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log.click()
time.sleep(5)
login = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login.click()
time.sleep(5)
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(MAIL)
password.send_keys(PASS)
password.send_keys(Keys.ENTER)

time.sleep(10)
allow = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[1]/span')
allow.click()
enable = driver.find_element_by_xpath('//*[@id="c366415127"]/div/div/div/div/div[3]/button[1]/span')
enable.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

time.sleep(7)
for _ in range(25):
    try:
        time.sleep(2)
        dislike = driver.find_element_by_xpath('//*[@id="c2094796203"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button/span/span/svg')
        dislike.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)
