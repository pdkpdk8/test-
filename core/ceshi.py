import pytest
from selenium import webdriver

'''<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">'''

chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe' #chrome_driver 存放位置
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://www.baidu.com/")
el1 = driver.find_element_by_id("kw")
el1.screenshot('2.png')
# el2 = driver.find_element_by_xpath('//*[@id="kw"]')
#1、强制等待 time.sleep（10）
#2、隐式等待 driver.implicitly_wait(10)
#3、显式等待
el2 = WebDriverwait(driver,10).until(
    lambda _:driver.find_element_by_xpath('//*[@id="kw"]')
)

print(el1)
print(el2)
print(el1.rect)  #元素的大小位置
print(el1.tag_name)  #元素的属性
el1.send_keys("demo")

driver.find_element_by_id("su").click()
driver.get_screenshot_as_file('1.png')
print('当前网址',driver.current_url) 
driver.quit()

# #编写测试用例
# #test_开头的文件，test_开头的函数，test_开头的类，用例中有断言
# def test_beifan():
#     assert 'bei=' == 'zhenshuai'

# #执行测试用例
# if __name__ == "__main__":
#     pytest.main()