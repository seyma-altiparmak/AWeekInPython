# PROTOTYPE - 1
# import our extension : https://github.com/mozilla/geckodriver/releases/tag/v0.32.1
from selenium import webdriver

#Escape \
# found the path
path = 'C:\\Users\seyma\Desktop\AWeekInPython\AWeekInPython\Day4\4 - Whatsapp Bot\geckodriver-v0.32.1-win64\geckodriver.exe'

#webbrowser selected and founded the path (geckodriver)
browser = webdriver.Firefox(executable_path = path)

# we found our website
browser.get('https://www.gamedevmarket.net/')

# Try-catch ex.
try:
    #we found our button
    browser.find_element_by_xpath("/html[1]/body[1]").click()
    print("Founded")
except:
    print("ERROR")

#refresh the page
browser.refresh()