import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import tkinter as tk
from tkinter import *

#driver = webdriver.Chrome()
chrome_options = Options()
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=chrome_options)

driver.get("http://www.javascriptkit.com/javatutors/detect-user-scroll-amount.shtml")
try:

    one  = driver.find_element_by_xpath('//*[@id="contentcolumn"]/h3[5]/a')
    two  = driver.find_element_by_xpath('//*[@id="contentcolumn"]/h3[5]/a')

    print(one)
    print(two)
    
    
except Exception as e:
    print('This is the error:',e)