import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

sekolah = "PUSUNGMALANG2"
password = '####'
listakun = []
with open('act.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         listakun.append([row['Email'], row['Password']])

for item in listakun:
    print(item[0])

login = "https://accounts.google.com/Login?hl=id&refresh=1%29%2C"

def klik(elemXPath):
    sleep(2)
    elemnya  = elemXPath 
    klikable = browser.find_element(By.XPATH,elemnya)
    browser.execute_script("arguments[0].click();", klikable) 

for item in listakun:
    browser = webdriver.Firefox()
    browser.execute_script("window.focus();")
    browser.get(login)
    failed = []
    try:
        sleep(5)
        browser.implicitly_wait(15)
        browser.find_element(By.ID,'identifierId').send_keys(item[0])
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
        sleep(5)
        browser.implicitly_wait(15)
        klik('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(item[1])
        browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
        sleep(5)
        browser.implicitly_wait(15)
        browser.find_element(By.ID,'accept').click()
        sleep(5)
        browser.implicitly_wait(15)
        browser.find_element(By.NAME,'Password').send_keys(password)
        browser.find_element(By.NAME,'ConfirmPassword').send_keys(password)
        browser.find_element(By.ID,'submit').click()
        sleep(5)
        browser.implicitly_wait(15)
        browser.save_screenshot("JPG/"+sekolah+'/'+item[0]+'.png')
        print('aktivasi sukses, menutup browser')
    except:
        failed.append(item)
        print("different pass")
    sleep(5)
    browser.implicitly_wait(15) 
    browser.close()
    sleep(3)

with open('failed.txt','w') as f:
    f.write(failed)