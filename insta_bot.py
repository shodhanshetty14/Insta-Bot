from selenium import webdriver
from time import sleep
from details import username, password, comment, followLst
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

import random

hashtag = ['python', 'javascript', 'React', 'Datascience', 'AI', 'automation', 'Cloud', 'bot']
post = []


class Instagram():
    def __init__(self):
        self.driver = webdriver.Firefox()


    def Open_Browser(self):
        self.driver.get('https://www.instagram.com/')
        self.driver.implicitly_wait(5)
        self.login()


    def login(self):
        login_block = self.driver.find_element(
            By.XPATH, '//input[@name = "username"]')
        password_block = self.driver.find_element(
            'xpath', '//input[@name="password"]')

        login_block.send_keys(username)
        password_block.send_keys(password)
        password_block.send_keys(Keys.ENTER)

        save_no_info = self.driver.find_element(
            'xpath', '/html/body/div[1]/section/main/div/div/div/div/button').click()
        no_notification = self.driver.find_element(
            'xpath', '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()


    def Like_comment_Hashtag(self):
        self.driver.get(
            'https://www.instagram.com/explore/tags/{}/'.format(hashtag[random.randint(0,2)]))
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            all_links = link.get_attribute('href')
            if ".com/p/" in all_links:
                post.append(all_links)
        for item in post:
            self.driver.get(item)
        

        # like btn loc
            like_btn = self.driver.find_element(
                'xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()

        # comment btn loc
            comment_box = self.driver.find_element(
                'xpath', '//textarea[@placeholder = "Add a comment…"]').send_keys(comment)
            post_btn = self.driver.find_element(
                'xpath', '//button[@type="submit"]').click()
            sleep(3)


    def SearchByUserName(self):
        
        # Itemvar1 = self.driver.execute_script("return prompt('Item name')") # this is not waiting for the user input and directly moves for next comment
        sender_name = pyautogui.prompt(text = 'Enter the username of the reciever',title='Reciever username', )
        self.driver.get('https://www.instagram.com/{}/'.format(sender_name))
        
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            all_links = link.get_attribute('href')
            if ".com/p/" in all_links:
                post.append(all_links)
        for item in post:
            self.driver.get(item)
        

        # like btn loc
            like_btn = self.driver.find_element(
                'xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()

        # comment btn loc
            comment_box = self.driver.find_element(
                'xpath', '//textarea[@placeholder = "Add a comment…"]').send_keys(comment)
            post_btn = self.driver.find_element('xpath', '//button[@type="submit"]').click()
            sleep(3)
        
        

    def FollowByUserName(self):
        # sender_name = pyautogui.prompt(text = 'Enter the username of the reciever',title='Reciever username' )
        # self.driver.get('https://www.instagram.com/{}/'.format(sender_name))
        for item in followLst:
            self.driver.get('https://www.instagram.com/{}/'.format(item))
            try:
                followbtn = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button').click()
                
            except:
                followbtn = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
            sleep(3)
            
bot = Instagram()
bot.Open_Browser()
sleep(3)
# bot.Like_comment_Hashtag()
# bot.SearchByUserName()
bot.FollowByUserName()

