import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import path, mkdir
from selenium.webdriver.firefox.options import Options

"""
ini adalah script yang ditulis tahun 2022
pengembangan di google selama ini membuat banyak alamat xpath halaman web google berubah  
dan tidak lagi sesuai dengan xpath yang tertulis pada script dan jika dijalankan anda mungkin menemui error
saat ini script ini masih dalam perbaikan (5 Nov 2024)
"""

wait = 5
sekolah = 'SMP'


options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

def klik(elemXPath):
    sleep(2)
    elemnya  = elemXPath 
    klikable = browser.find_element(By.XPATH,elemnya)
    browser.execute_script("arguments[0].click();", klikable) 

sekolah = 'JPG/'+sekolah

if path.exists('pass.txt'):
    print('file pass ready')
else :
    with open('pass.txt','w') as f:
        f.write('Password')


if path.exists('JPG'):
    print('folder ready')
else :
    mkdir('JPG')

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
    failed = []
    listakun = []
    with open('act.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['belajarid_email']!='':
                listakun.append([row['belajarid_email'], row['initial_password']])

    for item in listakun:
        print(item[0])

    login = "https://accounts.google.com/Login?hl=id&refresh=1%29%2C"

    for item in listakun:
        browser = webdriver.Firefox(options = options)
        browser.execute_script("window.focus();")
        browser.get(login)
        sleep(wait)
        
        try:
            browser.implicitly_wait(15)
            browser.find_element(By.ID,'identifierId').send_keys(item[0])
            browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button').click() #tombol login
            sleep(wait)
            browser.implicitly_wait(15)
            klik('/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
            browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(item[1])
            browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button').click() #selanjutnya
            sleep(wait)
            browser.implicitly_wait(15)
            try:
                browser.find_element(By.ID,'confirm').click()
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
                try:
                    print('proses reaktivasi')
                    browser.find_element(By.NAME,'Passwd').send_keys(password)
                    browser.find_element(By.NAME,'ConfirmPasswd').send_keys(password)
                    klik('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')
                    sleep(3)
                    try:
                        warni = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div[2]/span').text
                        print('gagal : '+warni)
                    except:
                        browser.save_screenshot(sekolah+'/'+item[0]+'.png')
                        print(f'reaktivasi {item[0]} sukses')
                except:
                    try:
                        sudahdiubah = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span').text
                        print(sudahdiubah)
                    except:
                        print('error lainnya, program masih berjalan, tunggu sampai selesai')
            
        except:
            failed.append(item)
            print(">>>>>different pass<<<<<")
        sleep(wait)
        browser.implicitly_wait(15) 
        #browser.close()
        sleep(3)

    text = ''
    for anu in failed:
        text+=''.join(anu)+'\n'

    with open('failed.csv','w') as f:
        f.write(text)
    print('proses selesai')
else:
    print('process aborted')
    
