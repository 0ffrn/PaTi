from selenium import webdriver
from time import sleep
import requests
import os

print("edita el script y pon el path de firefox donde pone executable_path porfa")
print('anonsurf start, cuando tengas todo listo lo ejecutas')

made_by_elmo = 1

while made_by_elmo == 1:
   r = requests.head("https://www.redbull.com/es-es/mejor-segundo-2020")
   r.status_code
   if r.status_code == 200:
      driver = webdriver.Firefox(executable_path="usr/share/applications/firefox.desktop")
      driver.get("https://www.redbull.com/es-es/mejor-segundo-2020")
      driver.find_element_by_xpath('//button[text()="Blon"]')\
         .click()
      os.system('anonsurf changeid')
      driver.refresh()
   elif r.status_code == 522:
      os.system('anonsurf changeid')
