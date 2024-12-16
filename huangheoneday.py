import requests
import datetime
import time
import re
import os
import sys
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

#reload(sys)
#sys.setdefaultencoding('utf-8')


localtime=time.strftime('%Y-%m',time.localtime(time.time()))
usepath='c:/hydrology/huanghe/'+localtime
isExists=os.path.exists(usepath)
if not isExists:
    os.makedirs(usepath)

os.chdir(usepath)
print (usepath)


now=datetime.datetime.now()

dateb=now.strftime('%Y-%m-%d %H:%M')
dateb=dateb.replace(' ','-')
dateb=dateb.replace(':','-')




driver = webdriver.Chrome()
driver.maximize_window()



filename=str("yellow"+dateb+".html")
tidefile=open(filename,'w')
driver.get('http://www.yrcc.gov.cn/gzfw/')
time.sleep(22)	
driver.find_element_by_xpath('//*[@id="zw"]/div[2]/div[2]/div[3]/ul/li/a/span').click()
time.sleep(10)

tabs = driver.window_handles
print(tabs)
print(len(tabs))
driver.switch_to.window(tabs[1])

shuju=driver.page_source
#shuju=shuju.encode('gbk')
tidefile.write(shuju)
tidefile.close()
time.sleep(10)


driver.close()
driver.quit()
driver = None