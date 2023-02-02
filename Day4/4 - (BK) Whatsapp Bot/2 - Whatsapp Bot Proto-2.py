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

browser.get('https://www.gamedevmarket.net/')



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

try:
    #we found our button
    browser.find_element_by_xpath("/html[1]/body[1]").click()
    print("Founded")
    #refresh the page
    browser.refresh()
except:
    print("ERROR")
    msg = "error"
    mail(msg)