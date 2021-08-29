
from selenium import webdriver
import time

#打开网址
driver = webdriver.Chrome()
driver.get("https://xp.chexinhui.com/xponclaim/#/login")

#等待页面加载完成


#查找元素
element_a = driver.find_element_by_name('username')
element_a.send_keys('xpadmin')
element_b = driver.find_element_by_name('password')
element_b.send_keys('12345')







