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
from webdriver_manager.chrome import ChromeDriverManager
 
root = tk.Tk()

#login function
def login(driver):
     #variables from gui
    username_text = username_input.get()
    password_text = password_input.get()
    limit_text = limit_input.get()

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
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        
        #remove notification if it pops up
        try:
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        except Exception as e:
            print('Click notification error:',e)
    except Exception as e:
        print('Login error:',e)

#like function
def like(driver,like_limit):
    clicked_arr = []
    queue_arr = []
    num_likes = 0

    while num_likes < like_limit:
        #put button into list
        try:
            like_buttons = driver.find_elements_by_css_selector('span.fr66n>button')
            print('Like buttons selected:',like_buttons)
        except Exception as e:
            print('Error selecting buttons.',e)

        #loop through buttons
        #try and click if it does not already exist in clicked_arr
        for button in like_buttons:
            if num_likes < like_limit:
                try:
                    #move to button
                    actions = ActionChains(driver)
                    actions.move_to_element(button).perform()

                    #append to clicked array
                    clicked_arr.append(button)
                    time.sleep(1)

                    #click button and incerement counter
                    button.click()
                    num_likes = num_likes + 1
                    print('Like number:',num_likes)
                    print('---')
                    print('---')
                    print('---')
                    print('An element was clicked:',button)
                    print('---')
                    print('---')
                    print('---')
                    time.sleep(1)
                except Exception as e:
                    print('Error clicking for',button)
                    print('Error message',e)

        time.sleep(5)

        # re-analyze DOM. Jump to last item in list
        print('-')
        print('--')
        print('---')
        print('----')
        print('-----')
        print('------')
        print('-------')
        print('Reanalyzing...once last element is no longer in DOM, new elements will be ready to be clicked.')
        print('-------')
        print('------')
        print('-----')
        print('----')
        print('---')
        print('--')
        print('-')

        #scroll to top to get the correct 'last_button' needed after first iteration
        try:
            driver.execute_script("window.scrollTo(0,0)")
            reanalyzed_buttons = driver.find_elements_by_css_selector('span.fr66n>button')
            print('reanalyzed buttons',reanalyzed_buttons)
            last_button = reanalyzed_buttons[-1]
            last_button_scroll_height = last_button.location['y']
            print('last button:',last_button)
            print('last button scroll height',last_button_scroll_height)
        except Exception as e:
            print('Re-analayze issue:',e)

        #place listener on last item
        #jump to last item
        try:
            driver.execute_script("window.scrollTo(0,"+str(last_button_scroll_height)+")")
            print('jump performed')
        except Exception as e:
            print('jump error:',e)
        
        #programatically scroll and stop once listener detects that the last button has been removed from the DOM
        scroll_continue = True
        
        while scroll_continue:
            print('scroll')
            time.sleep(1)

            #determine if element still exists by trying to scroll to it
            try:
                actions = ActionChains(driver)
                actions.move_to_element(last_button).perform()
                print('rescroll performed')
            except Exception as e:
                print('Last button in list no longer exists...new elements are available')
                scroll_continue = False
            #if it does not...stop scrolling
            else:
                print('Total scroll:',last_button_scroll_height)
                driver.execute_script("window.scrollTo(0,"+str(last_button_scroll_height)+")")
                last_button_scroll_height = last_button_scroll_height+500
                scroll_continue = False

    #scroll to top
    driver.execute_script("window.scrollTo(0,0)")
    
    print('scrolled to top.')
    print('All elements that were clicked:',clicked_arr)

    time.sleep(5)

    #like_buttons[0].find_element_by_tag_name('button').click()
    return clicked_arr
#************************************************************************************************
#************************************************************************************************
#************************************************************************************************
#************************************************************************************************
#************************************************************************************************

#general process
def launch(config):
    chrome_options = Options()
    #driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://instagram.com")
    
    #login
    login(driver)

    #enter while loop for a specified number of iterations
    like_limit = int(limit_input.get())
    like(driver,like_limit)

    print('EVERYTHING WAS CLICKED CORRECTLY!!!')

#************************************************************************************************
#************************************************************************************************
#************************************************************************************************
#************************************************************************************************
#************************************************************************************************
#tkinter
canvas = tk.Canvas(root,height=600,width=500,bg="#ddd")
canvas.pack()

background = '#ddd'

#app header
header = Label(root,text="Instagram 'Like' Bot",font=("Helvetica",40),bg=background)
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

#limit label
limit_label = Label(root, text="like limit", font=("Helvetica",14),bg=background)
canvas.create_window(250,410,window=limit_label)

#limit input
limit_input = tk.Entry(root)
canvas.create_window(250,440,window=limit_input)

#limit dropdown


#submit button
button = tk.Button(text='Submit', command=lambda:launch(config))
canvas.create_window(250, 500, window=button)

#build GUI
root.resizable(False, False)
root.mainloop()






