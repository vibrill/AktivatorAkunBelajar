import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path, mkdir

wait = 5
sekolah = 'coba'

def klik(elemXPath):
    sleep(2)
    elemnya  = elemXPath 
    klikable = browser.find_element(By.XPATH,elemnya)
    browser.execute_script("arguments[0].click();", klikable) 

sekolah = 'JPG/'+sekolah
if path.exists(sekolah):
    print('folder ready')
else :
    mkdir(sekolah)
password = ''
with open('pass.txt','r') as f:
    password = f.read()
print(password)
ask = input(f'sekolah yang diproses = {sekolah}\npasword yang digunakan = {password}\napakah benar? y/n ')
if ask == 'y':
    listakun = []
    with open('act.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['belajarid_email']!='':
                listakun.append([row['belajarid_email'], row['belajarid_initial_password']])

    for item in listakun:
        print(item[0])

    login = "https://accounts.google.com/Login?hl=id&refresh=1%29%2C"

    for item in listakun:
        browser = webdriver.Firefox()
        browser.execute_script("window.focus();")
        browser.get(login)
        sleep(wait)
        failed = []
        try:
            browser.implicitly_wait(15)
            browser.find_element(By.ID,'identifierId').send_keys(item[0])
            browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
            sleep(wait)
            browser.implicitly_wait(15)
            klik('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
            browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(item[1])
            browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
            sleep(wait)
            browser.implicitly_wait(15)
            browser.find_element(By.ID,'accept').click()
            sleep(wait)
            browser.implicitly_wait(15)
            browser.find_element(By.NAME,'Password').send_keys(password)
            browser.find_element(By.NAME,'ConfirmPassword').send_keys(password)
            browser.find_element(By.ID,'submit').click()
            sleep(wait)
            browser.implicitly_wait(5)
            try :
                klik('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
                browser.implicitly_wait(10)
                klik('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
                browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(password)
                sleep(2)
                browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(Keys.ENTER)
                print('verified')
            except:
                print('no need verification')
            sleep(wait)
            browser.implicitly_wait(15)
            browser.save_screenshot(sekolah+'/'+item[0]+'.png')
            print(f'aktivasi {item[0]} sukses, menutup browser')
        except:
            failed.append(item)
            print(">>>>>different pass<<<<<")
        sleep(wait)
        browser.implicitly_wait(15) 
        browser.close()
        sleep(3)

    text = ''
    for anu in failed:
        text+=''.join(anu)+'\n'

    with open('failed.csv','w') as f:
        f.write(text)
else:
    print('process aborted')
    