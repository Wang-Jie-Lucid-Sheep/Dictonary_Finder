# Profile
This is a python script that could find words means from Cambridge Dictionary automatically.

This is another Python script for automatic load to the shcool network.



# Instuall Selenium
## Install Selenium
```shell
pip install selenium==3.141.0
```

## Install Selenium Tool
```shell
pip install msedge-selenium-tools
```

## Change Library Version
```shell
pip uninstall urllib3
pip install urllib3==1.26.2
```
## Download Wed Driver
This is Edge driver:*[Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver?form=MA13LH)*


# Used Grammar
## Load a Web
```python
from selenium import webdriver  #web library
from msedge.selenium_tools import Edge, EdgeOptions #tools
import time #time delay library
options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"Browser Path"
driver = Edge(options=options, executable_path=r"Driver Path")
driver.get("Web Address")
```
##  Wait the web load
```python
import time
time.sleep(2)
```
## Stop web load
```python
try:   #open the web
    driver.set_page_load_timeout(5)#automatically stop loading after a timeout of three seconds
    driver.get("Web Address")
except Exception as e:
     print(e)
# other code
```
## Input box
```python
input_box = driver.find_element_by_xpath('Input_Box_Xpath')
input_box.send_keys("line")
```

## Clean input box
```python
input_box = driver.find_element_by_xpath('Input_Box_Xpath')
input_box.clear()
```
## Touch a Button
```python
search_bottom = driver.find_element_by_xpath('Button_Xpath')
search_bottom.click()
```
## Force button click
```python
driver.get("Web Address")
confirm_button = driver.find_element_by_xpath('Button_Xpath')
driver.execute_script("arguments[0].click();",confirm_button)
```
## Select list Usage
```python
from selenium.webdriver.support.select import Select #The 'Select' class library
select_list_box = driver.find_element_by_xpath('Select_Box_Xpath')
Select_Box = Select(select_list_box) #New a 'Select' class
Select_Box.select_by_value('object of being selected')
```
## Screen clip from web
```python
driver = Edge(options=options, executable_path=r"Driver Path")
driver.get("Web Address")
driver.get_screenshot_as_file("photo_name")
```
