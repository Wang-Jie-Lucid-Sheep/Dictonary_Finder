from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
import time
options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"E:\河海大学\学习笔记\Python\Project\msedgedriver.exe") # 相应的浏览器的驱动位置
try:
    driver.set_page_load_timeout(5)#automatically stop loading after a timeout of three seconds
    driver.get("https://dictionary.cambridge.org/dictionary/english/")
except Exception as e:
     print(e)
#switch_bottom = driver.find_element_by_link_text('English')
#switch_bottom.click()
#time.sleep(1)
#input_box = driver.find_element_by_id('stateSearchAutocomplete')
#input_box = driver.find_element_by_class_name('pa p0 pl0 chsw lc1 lp-l_l-5 maxz')
input_box = driver.find_element_by_xpath('//*[@id="searchword"]')
input_box.send_keys('python')
#search_bottom = driver.find_element_by_class_name('bo iwc iwc-40 hao lb0 cdo-search-button lp-0')
search_bottom = driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/div[1]/span/button[3]')
try:
    driver.set_page_load_timeout(10)#automatically stop loading after a timeout of three seconds
    search_bottom.click()
except Exception as e:
     print(e)
1+1


#print(input_box)
