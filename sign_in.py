# coding=gbk
from selenium import webdriver
import time
import random
import string
import sys

try:
    user = os.environ["username"]
    pwd = os.environ["password"]
    location = os.environ["location"]
except:
    print("�����������������û���������͵ص��Ƿ���ȷ��д")
    exit(1)

browser = webdriver.Chrome()
browser.get("https://www.dxever.com/fei/delete/ncp/login.html")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="box"]/input[1]').send_keys(user)
browser.find_element_by_xpath('//*[@id="box"]/input[2]').send_keys(pwd)
browser.find_element_by_xpath('//*[@id="box"]/button').click()
time.sleep(1)

try:
    browser.find_element_by_xpath('//*[@id="item"]/ul/li[1]/input')
except:
    print("�û������������")
    exit(1)

browser.find_element_by_xpath('//*[@id="item"]/ul/li[1]/input').send_keys(location)
browser.find_element_by_xpath('//*[@id="item"]/ul/li[2]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[3]/div/input[1]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[4]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[5]/div/input[3]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[6]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/ul/li[7]/div/input[2]').click()
browser.find_element_by_xpath('//*[@id="item"]/div/button').click()
time.sleep(1)

    

browser.get("https://www.dxever.com/fei/delete/ncp/history.html")
if "����" in browser.page_source:
    print("ǩ���ɹ�")
else:
    print("ǩ��ʧ��")
    exit(0)
