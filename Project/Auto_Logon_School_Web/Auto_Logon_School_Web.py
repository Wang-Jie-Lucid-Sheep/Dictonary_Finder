from selenium import webdriver  #web library
from selenium.webdriver.support.select import Select  #Select class
from msedge.selenium_tools import Edge, EdgeOptions #tools
import time #time delay library

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"E:\河海大学\学习笔记\Python\Dictonary_Finder\Project\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get("http://10.255.0.19/")

exit_button = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div/form/input')
#exit_buttom.click()
driver.execute_script("arguments[0].click();",exit_button)

time.sleep(2)

confirm_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/input[1]')
#confirm_buttom.click()
time.sleep(1)
driver.execute_script("arguments[0].click();",confirm_button)

names = ' '
keys = ' '

time.sleep(1)
#driver.refresh()
driver.get("http://10.255.0.19/")

time.sleep(3)
load_button = driver.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/form/input[2]')
input_name = driver.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/form/input[3]')
input_password = driver.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/form/input[4]')
select_list_box = driver.find_element_by_xpath('//*[@id="edit_body"]/div[4]/div[1]/select')
Select_Box = Select(select_list_box)

Select_Box.select_by_value('@unicom')
input_name.send_keys(names)
input_password.send_keys(keys)


#load_button.click()
driver.execute_script("arguments[0].click();",load_button)
