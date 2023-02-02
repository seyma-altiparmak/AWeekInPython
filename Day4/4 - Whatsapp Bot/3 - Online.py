# PROTOTYPE - 1
# import our extension : https://github.com/mozilla/geckodriver/releases/tag/v0.32.1
# I do not have extra google account thats why i randomize that:
# email = youremailishere@gmail.com (our server)
# password = emailconfig123
# less protected application is OPENED. in google

from selenium import webdriver
import smtplib #our lib. for this job

path = 'C:\\Users\seyma\Desktop\AWeekInPython\AWeekInPython\Day4\4 - Whatsapp Bot\geckodriver-v0.32.1-win64\geckodriver.exe'

browser = webdriver.Firefox(executable_path = path)

browser.get('https://web.whatsapp.com/')



def mail(message):
    owner='youremailishere@gmail.com'
    receiver = 'tel.email.ishere@gmail.com'
    logIn = 'youremailishere@gmail.com'
    password = 'emailconfig123'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(logIn,password)
    server.sendmail(owner,receiver,message)
    server.quit()

control = True
control2 = True

while True:
    try:
        #we found our button online or named "çevrimiçi"
        browser.find_element_by_xpath("//span[text() = 'online']").click()
        if control == True:
            msg2 = "ONLINE GO! GO! GO!"
            mail(msg2)
            control =False
            control2 = True
    except:
        control = False
        if control2 == True:
            msg = "Safe Area"
            mail(msg)
            control2 = False