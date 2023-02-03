from selenium import webdriver
import time

path = 'C:\\Users\seyma\Desktop\AWeekInPython\AWeekInPython\Day5\5\geckodriver-v0.32.1-win64'
browser = webdriver.Firefox(executable_path = path)
browser.get('https://www.instagram.com')
user = browser.find_element_by_xpath("//input[contains(@name,'username')]")
password = browser.find_element_by_xpath("//input[contains(@name,'password')]")
username = input("your nickname:")
yourFollowerNum = input("Following people:")
user.send_key("accountName")
password.send_key("accoundPassword")
browser.find_element_by_xpath("//div[contains(text(), 'Yap')]").click()
browser.get('https://www.instagram.com/{}/'.format(username))
x = 1
time.sleep(2)
while True:
    #Giris yapildi
    time.sleep(2)
    browser.find_element_by_xpath("//header/section[1]/ul[1]/li[3]/a[1]/div[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[{}]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/span[1]/div[1]".format(x)).click()
    time.sleep(1)
    if (browser.find_element_by_xpath("//div[contains(text(),'{}')]".format(username))) == True:
        time.sleep(1)
        browser.get('https://www.instagram.com/{}/'.format(username))
    else:
        print(browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/h2[1]"))
        browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]").click()
        time.sleep(1)
        browser.find_element_by_xpath("//header/section[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
        time.sleep(1)
        browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[7]/div[1]").click()
        time.sleep(2)
        browser.get('https://www.instagram.com/{}/'.format(username))
    time.sleep(2)
    x = x+1
    if yourFollowerNum < x:
        break
