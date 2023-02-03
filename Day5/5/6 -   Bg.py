#Background
from selenium import webdriver
import time

accountNum = 1
print("""
Welcome
1- Follow
2- Like
3- Comment
""")
inputbot = input("Your selection:")

if inputbot=="1":
    name = input("User Name:")
    control = 1
elif inputbot=="2":
    link = input("Link:")
    control2 = 1
elif inputbot == "3":
    link = input("Link:")
    comment = inputbot("Your Comment:")
    control3 = 1

#here
settings = webdriver.FirefoxOptions()
settings.headless = True
#Firstly Log in:
path = 'C:\\Users\seyma\Desktop\AWeekInPython\AWeekInPython\Day5\5\geckodriver-v0.32.1-win64'
browser = webdriver.Firefox(options = settings,executable_path = path)
browser.get('https://www.instagram.com/')
user = browser.find_element_by_xpath("//input[contains(@name,'username')]")
password = browser.find_element_by_xpath("//input[contains(@name,'password')]")
user.send_keys("denemeinstabot"+str(accountNum))
password.send_keys("123456.Bot")
browser.find_element_by_xpath("//div[contains(text(), 'Yap')]").click()
time.sleep(2)

while True:
    #controlers:
    if control == 1:
        print("follow started...")
        browser.get('https://www.instagram.com/{}/'.format(name))
        time.sleep(2)
        browser.find_element_by_xpath("//button[contains(text(),'Et')]").click()
    if control2 ==1:
        print("like started...")
        browser.get(link)
        time.sleep(2)
        browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[3]/div[1]/div[1]/section[1]/span[1]/button[1]").click()
    if control3 ==1:
        print("comment started...")
        browser.get(link)
        time.sleep(2)
        browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[3]/div[1]/div[1]/section[1]/span[2]/button[1]").click()
        time.sleep(2)
        browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/div[1]/article[1]/div[1]/div[3]/div[1]/div[1]/section[3]/div[1]/form[1]/div[1]/textarea[1]").send_keys(comment)
        time.sleep(2)

#sleep
    time.sleep(10)
    print("Done" + str(accountNum))

#log-out
    browser.get('https://www.instagram.com/denemeinstabot/')
    time.sleep(1)
    browser.find_element_by_xpath("//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[1]/button[1]/div[1]/svg[1]/circle[1]").click()
    browser.find_element_by_xpath("//button[contains(text(),'Yap')]").click()

    if accountNum> 3: #for 2 account i+1 is here
        break
    else:
        accountNum = accountNum+1

