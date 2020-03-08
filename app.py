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

root = tk.Tk()

#like function
def like(driver,clicked_elements):
    clicked_arr = clicked_elements
    queue_arr = []
    

    try:
        like_buttons_container = driver.find_elements_by_class_name('fr66n')
    except Exception as e:
        print('Error selecting class.',e)

    #put into global clicked_arr and queue_arr for this iteration
    for items in like_buttons_container:
        try:
            like_button = items.find_element_by_tag_name('button')
            if like_button not in clicked_arr:
                clicked_arr.append(like_button)
                queue_arr.append(like_button)
        except Exception as e:
            print('Outter Loop error',e)

    #iterate and click
    print('Queue before loop:',queue_arr)
    for button in queue_arr:
        print('b4')
        actions = ActionChains(driver)
        actions.move_to_element(button).perform()
        print('af')
        print('scroll performed for:',button)
        time.sleep(2)
        
        try:
            button.click()
            print('---')
            print('---')
            print('---')
            print('An element was clicked:',button)
            print('---')
            print('---')
            print('---')
        except Exception as e:
            print('Error clicking for',button)

    #like_buttons[0].find_element_by_tag_name('button').click()
    print('Clicked array for this iteration:',clicked_arr)
    final_element = clicked_arr[len(clicked_arr)-1]
    return clicked_arr

def login(driver):
     #variables from gui
    username_text = username_input.get()
    password_text = password_input.get()

    try:
        #enter info
        time.sleep(2)
        
        #grab elements
        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        
        #send GUI info to elements
        user_name.send_keys(username_text)
        password.send_keys(password_text)

        #click login
        time.sleep(2)
        #driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        
        #remove notification if it pops up
        try:
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except Exception as e:
            print('Click notification error:',e)
    except Exception as e:
        print('Login error:',e)

#general process
def launch(config):
    chrome_options = Options()
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=chrome_options)
    driver.get("https://instagram.com")
    
    #login
    login(driver)

    #clicked elements
    done_elements = []

    #enter while loop for a specified number of iterations
    i = 0
    scroll_height = 0
    while i < 4:
        print('Iteration number:',i)
        x = like(driver,done_elements)
        done_elements = x
        i = i+1

    print('while loop ended')
    print('Clicked Elements:',done_elements)
    print('EVERYTHING WAS CLICKED CORRECTLY!!!')



#tkinter
canvas = tk.Canvas(root,height=500,width=500,bg="#ddd")
canvas.pack()

background = '#ddd'

#app header
header = Label(root,text="Instagram Social Tool",font=("Helvetica",40),bg=background)
canvas.create_window(250,100,window=header)

#username label
username_label = Label(root, text="username", font=("Helvetica",14),bg=background)
canvas.create_window(250,170,window=username_label)

#usename input
username_input = tk.Entry(root)
canvas.create_window(250,200,window=username_input)

#password label
password_label = Label(root, text="password", font=("Helvetica",14),bg=background)
canvas.create_window(250,290,window=password_label)

#password input
password_input = tk.Entry(root,show="*")
canvas.create_window(250,320,window=password_input)

#submit button
button = tk.Button(text='Submit', command=lambda:launch(config))
canvas.create_window(250, 420, window=button)

#build GUI
root.resizable(False, False)
root.mainloop()






