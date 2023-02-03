#Seri takip isteği
from selenium import webdriver
import time

path = 'C:\\Users\seyma\Desktop\AWeekInPython\AWeekInPython\Day5\5\geckodriver-v0.32.1-win64'
browser = webdriver.Firefox(executable_path =path)
browser.get('https://www.instagram.com')

accountName = input("Your nickname is:")

x = 1
while True:
    user = browser.find_element_by_xpath("//input[contains(@name,'username')]")
    password = browser.find_element_by_xpath("//input[contains(@name,'password')]")
    user.send_key(accountName)
    password.send_key("accoundPassword")
    browser.find_element_by_xpath("//div[contains(text(), 'Yap')]").click()
    time.sleep(2)
    browser.get('https://www.instagram.com/explore/people/')
    time.sleep(2)
    browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[{}]/div[3]/button[1]".format(x)).click()
    time.sleep(1)
    x+=1
    time.sleep(1)
    browser.get('https://www.instagram.com/{}/'.format(accountName))
    time.sleep(1)
    browser.find_element_by_xpath("//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[1]/button[1]/div[1]/svg[1]/circle[1]").click()
    browser.find_element_by_xpath("//button[contains(text(),'Yap')]").click()
    
    if x ==30:
        break