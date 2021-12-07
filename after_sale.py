from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time

#登录账号
driver = webdriver.Chrome()
driver.get("https://demob.86yfw.com/home/login")

element_login = driver.find_element_by_name('login_name').send_keys('testpdd')
element_pwd = driver.find_element_by_name('password').send_keys('123456')

element_loginBtn = driver.find_element_by_id('submitBtn').click()

#查询订单1
element_orderInput = driver.find_element_by_css_selector('input.layui-input').send_keys('15')
element_loginBtn = driver.find_element_by_class_name('layui-icon search_btn layui-icon-search').click()


#拼多多协商历史--商家同意退款
element_agreeBtn = driver.find_element_by_class_name('layui-btn layui-btn-sm pdd_refund').click()
element_agreeBtn_1 = driver.find_element_by_css_selector('a.layui-layer-btn0').click()