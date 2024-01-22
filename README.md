# Profile
This is a python script that could find words means from Cambridge Dictionary automatically.

This is another Python script for automatic load tothe shcool network.



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
##  Wait the web load
```python
import time
time.sleep(2)
```
## Stop web load
```python
try:   #open the web
    driver.set_page_load_timeout(5)#automatically stop loading after a timeout of three seconds
    driver.get("https://dictionary.cambridge.org/dictionary/english/")
except Exception as e:
     print(e)
# other code
```
## Clean input box
```python
input_box = driver.find_element_by_xpath('//*[@id="searchword"]')
input_box.clear()
```
