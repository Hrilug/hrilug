from selenium import webdriver
from time import sleep

drive = webdriver.Chrome(executable_path='chromedriver.exe')
drive.get('https://www.bilibili.com')
 
drive.find_element_by_class_name('bili-avatar')

sleep(2)
drive.close()