import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk
from tkinter import *

root = tk.Tk()

#scroll function
def scroll():
    driver.execute_script("window.scrollTo(0,8000)") 

#like function
def like():
    like_buttons = driver.find_elements_by_class_name('fr66n')
    for items in like_buttons:
        items.find_elements_by_class_name('wp0rb')

#general process
def login(config,loop_limit):
    #variables from gui
    username_text = username_input.get()
    password_text = password_input.get()
    print('username',username_text)
    print('password',password_text)

    #driver = webdriver.Chrome()
    chrome_options = Options()
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=chrome_options)
    
    #instagram 
    driver.get("https://instagram.com")
    
    try:
        # click login button
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()

        #enter info
        time.sleep(2)
        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        
        user_name.send_keys(username_text)
        password.send_keys(password_text)

        #click login
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
        
        #remove notification if it pops up
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

    #     #enter while loop for a specified number of iterations
    #     i = 0
    #     while i < loop_limit:
    #         #scroll down to load more content
    #         time.sleep(2)
    #         scroll()
            
    #         #gather all like buttons and iterate
    #         time.sleep(2)
    #         like()
            
    #         #iterate
    #         i = i+1
        
    #     #out of loop
    #     print('loop ended')

    except Exception as e:
        print(e)


canvas = tk.Canvas(root,height=500,width=500,bg="#263D42")
canvas.pack()

#username label
username_label = Label(root, text="username", font=("Helvetica",14))
canvas.create_window(250,100,window=username_label)

#usename input
username_input = tk.Entry(root)
canvas.create_window(250,150,window=username_input)

#password label
password_label = Label(root, text="password", font=("Helvetica",14))
canvas.create_window(250,200,window=password_label)

#password input
password_input = tk.Entry(root)
canvas.create_window(250,250,window=password_input)

#submit button
button = tk.Button(text='Get the Square Root', command=lambda:login(config,10))
canvas.create_window(250, 300, window=button)

#build GUI
root.resizable(False, False)
root.mainloop()






