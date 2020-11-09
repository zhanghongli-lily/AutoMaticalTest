from selenium import webdriver

import time
import  os
# #
# option = webdriver.ChromeOptions()
# option.binary_location = r'C:\Users\Lily\pythonProject\com\lily\chromedriver.exe'
driver = webdriver.Chrome()
# driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.126.com")

print('Before login================')

#打印当前⻚⾯title
title=driver.title
print(title)
#
#
# import logging
#
# logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')