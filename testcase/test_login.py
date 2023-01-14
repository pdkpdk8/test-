import pytest
from selenium import webdriver
from core.data import read_csv,read_excel
import time
from selenium.webdriver.support.ui import Select

'''<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">'''
#创建夹具，可以指定夹具的共享范围，同一个范围内的用例可以使用同一个夹具，夹具共享范围有5个
# function  默认
# class    
# Module  
# package
# session
@pytest.mark.parametrize(
    "username,password,msg",
    read_csv("ddt_test_login.csv"),
)
def test_baidu(driver,username,password,msg):
    time.sleep(2)
    ipt_username = driver.find_element_by_xpath('//*[@id="q"]')
    # print(el1.rect)  #元素的大小位置
    # print(el1.tag_name)  #元素的属性
    assert ipt_username.tag_name == "input"
    ipt_username.send_keys(username)
    ipt_username.screenshot('1.png')
    # print('当前网址',driver.current_url) 
    time.sleep(2)

def test_screenshot(driver):
    btn = driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
    assert btn.text == "搜索"
    btn.click()
    driver.get_screenshot_as_file('2.png')
    time.sleep(2)


@pytest.mark.parametrize(
    "name,tel,province,city,county,address,alias,msg",
    read_excel("ddt_test_new_address.xlsx"),
)
def test_address(address,name,tel,province,city,county,ads,alias,msg):
    #地址信息
    #非 select 下拉框的解决办法,先激活下拉框   
    # adr = address.find_element_by_xpath('//*[@id="cndzkEntrance"]/div[2]/div/div/div[1]/div/span[1]')
    # time.sleep(1)
    # js = '''
    # document.querySelector("#cndzkEntrance > div:nth-child(2) > div > div > div > div > span.cndzk-entrance-division-header-click-input")
    # '''
    # address.execute_script(js)

    # adr.clear()
    # adr.send_keys('北京/北京市/东城区/东华门街道')
    print("请手动输入地址")
    time.sleep(10)
    #详细地址
    ipt_address = address.find_element_by_xpath('//*[@id="cndzkEntrance"]/div[4]/div/div/textarea')
    ipt_address.send_keys('111222333444')
    #收货人姓名
    ipt_name = address.find_element_by_xpath('//*[@id="fullName"]')
    ipt_name.send_keys('顾明珠')
    #手机号码
    ipt_phone = address.find_element_by_xpath('//*[@id="mobile"]')
    ipt_phone.send_keys('18768111111')
    #提交
    btn = address.find_element_by_xpath('//*[@id="myForm"]/div[5]/div[2]/button')
    btn.click()

    assert 1==msg
    address.get_screenshot_as_file('3.png')
