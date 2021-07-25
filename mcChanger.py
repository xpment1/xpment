# a3cxxzdz4vuk

# sudo macchanger -m 70:BB:E9:69:1F:BE wlp2s0
# 76:09:2B:F5:8A:69

# LAPTOP-DJSCT23I
# HUAWEI_nova_3e-3314bfd5f9
# Chromecast
# saurav-Lenovo-G50-70
# Pixel-3-XL




# import requests, time

# while True:
#     try:
#         x = requests.get('https://1.1.1.1/dns/')

#         print(x.status_code)
#         time.sleep(2)

#         print("-----------------------")
#     except:
#         print("Not connected")


# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Time =", current_time)
 

# import os
# import subprocess


# sudoPassword = 'F!retornado9'
# command1 = 'ifconfig wlp2s0 down'
# command2 = 'macchanger -r wlp2s0'
# command3 = 'ifconfig wlp2s0 up'
# p = os.system('echo %s|sudo -S %s' % (sudoPassword, command1))
# p = os.system('echo %s|sudo -S %s' % (sudoPassword, command2))
# p = os.system('echo %s|sudo -S %s' % (sudoPassword, command3))


# import schedule
# import requests
# import os
# import subprocess
# import time
# from datetime import datetime


# def macChanger():
    
#     sudoPassword = 'F!retornado9'
#     command1 = 'ifconfig wlx001e2ad2b5bd down'
#     command2 = 'macchanger -r wlx001e2ad2b5bd'
#     command3 = 'ifconfig wlx001e2ad2b5bd up'
#     p = os.system('echo %s|sudo -S %s' % (sudoPassword, command1))
#     p = os.system('echo %s|sudo -S %s' % (sudoPassword, command2))
#     p = os.system('echo %s|sudo -S %s' % (sudoPassword, command3))


# def job(t):
#     print ("I'm working...", t)
#     return

# schedule.every().day.at("18:39").do(macChanger)

# while True:
#     schedule.run_pending()
#     time.sleep(60) # wait one minute
 


# macChanger()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# need the below imports to work with Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('thewebpage')

search = browser.find_element_by_id('getSearch')
search.click()
search.send_keys('searchitem' + Keys.RETURN)

searchitem = browser.find_elements_by_class_name("name")[0]
searchitem.click()

# Here is the logic that we have to update

# Get number of users rather than the users.
userElems = len(browser.find_elements_by_link_text("#/user/"))

# iterate through each user by using the index
  # if you try to use the find_elements as shown in OP, you will get StaleElement Exception
  # because the user elements references will be refreshed when navigated to next page and
  # load back (so we have to find the elements based on index on the page every time)

for userNum in range(1,userElems):
    # this below explicit wait will make sure the script will wait max 30 sec for the next user to be clicked
    user = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"(#/user/)[" + str(userNum) + "]")))
    # scroll user into view
    user.location_once_scrolled_into_view
    # click on user
    user.click()
    # click on follow link
    follow = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"followAction")))
    follow.click()
    # click on browser back button
    browser.back()
