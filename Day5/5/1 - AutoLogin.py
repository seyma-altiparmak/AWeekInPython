# AUTOLOGIN
# email = "denemeinstabot2023@gmail.com"
# password = "123456.Bot"

from selenium import webdriver
import time

path = "C:\Users\seyma\Desktop\AWeekInPython\AWeekInPython\Day5\geckodriver-v0.32.1-win64"
browser = webdriver.Firefox(executable_path=path)

browser.get('https://www.instagram.com/')

user = browser.find_element_by_xpath("//input[contains(@name,'username')]")
password = browser.find_element_by_xpath("//input[contains(@name,'password')]")
user.send_keys("denemeinstabot")
password.send_keys("123456.Bot")

browser.find_element_by_xpath("//div[contains(text(), 'Yap')]").click()
