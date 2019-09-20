# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:15:48 2019

@author: sabv2e15338
"""

#E PAPER PYTHON
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#DISPLAY MESSAGE BOX
import pymsgbox
import time
#USING THE KEYBOARD KEYS WE NEED TO IMPORT
import keyboard
#GET THE CURRENT DATE AS MENTION IN DIRECTORY
from datetime import date
#IMPORT OS TO CREATE A FOLDER DIRECTORY IN PATH
import os
import pyautogui

#GET CURRENT DATE
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d-%m-%Y")
pymsgbox.alert('The current date is:', d1)
response = pymsgbox.prompt(d1,timeout=2000 )


#CREATING THE PATH
dirName = 'D:\\'+str(d1)+'\\Central Chronicle Epaper'
def main():
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists") 
        time.sleep(2)
if __name__ == '__main__':
     main()

#C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
driver = webdriver.Chrome(executable_path='path')

print("The chrome is launched")

driver.maximize_window()

driver.get('https://www.centralchronicle.com/epaper/')

pagelength = driver.find_elements_by_class_name("menu")

a=len(pagelength)
print(a)
time.sleep(3)
pymsgbox.alert('The Bhopal edition page length: ', a)

response = pymsgbox.prompt(a,timeout=1000)

for elem in range (2, a):
    try: 
        driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table/tbody/tr['+ str(elem)+']/td/a').click();
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a[1]').click();
        #downloadclick.send_keys("ctrl+S")
        time.sleep(4)
        keyboard.press_and_release('ctrl+S')
        #print(savename)
        time.sleep(2)
        
        copyname = pyautogui.hotkey('ctrl', 'x')   
        response = pymsgbox.prompt(copyname,timeout=2000 )
        
        time.sleep(0.5)
        
        keyboard.write(dirName+'\\')
        pyautogui.hotkey('ctrl', 'v')
        
        firstenter = pyautogui.press('enter')
        print("The path set:",firstenter)
        
        time.sleep(2)
        pyautogui.press('ctrl','w')
        pass
    except Exception as ex:
        print(ex)
        pass
    finally:
        driver.close()
        logger.info("Chrome driver closed...")
        driver.quit()
        logger.info("chrome driver is quited")
    
    
