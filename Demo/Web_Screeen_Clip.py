from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from time import sleep
options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"E:\河海大学\学习笔记\Python\Project\msedgedriver.exe") # 相应的浏览器的驱动位置

driver.get("https://dictionary.cambridge.org/")
sleep(3)
driver.get_screenshot_as_file("capter.png")
