#AUTO LOG OUT
# email = "denemeinstabot2023@gmail.com"
# password = "123456.Bot"

from selenium import webdriver
import time

#Firstly Log in:
path = 'C:\\Users\seyma\Desktop\AWeekInPython\AWeekInPython\Day5\5\geckodriver-v0.32.1-win64'
browser = webdriver.Firefox(executable_path = path)
browser.get('https://www.instagram.com/')
user = browser.find_element_by_xpath("//input[contains(@name,'username')]")
password = browser.find_element_by_xpath("//input[contains(@name,'password')]")
user.send_keys("denemeinstabot")
password.send_keys("123456.Bot")
browser.find_element_by_xpath("//div[contains(text(), 'Yap')]").click()

#sleep
time.sleep(10)

#log-out
browser.get('https://www.instagram.com/denemeinstabot/')
time.sleep(1)
browser.find_element_by_xpath("//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[1]/button[1]/div[1]/svg[1]/circle[1]").click()
browser.find_element_by_xpath("//button[contains(text(),'Yap')]").click()