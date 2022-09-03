from selenium import webdriver
from time import sleep
from details import username, password, comment
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import random

hashtag = ['python', 'javascript', 'React']
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
            'https://www.instagram.com/explore/tags/{}/'.format('programming'))
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            all_links = link.get_attribute('href')
            if ".com/p/" in all_links:
                post.append(all_links)
        for item in post:
            self.driver.get(item)
        # self.driver.get('https://www.instagram.com/p/Ch_XqUEMvue/')

        # like btn loc
            like_btn = self.driver.find_element(
                'xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()

        # comment btn loc
            comment_box = self.driver.find_element(
                'xpath', '//textarea[@placeholder = "Add a comment…"]').send_keys(comment)
            post_btn = self.driver.find_element(
                'xpath', '//button[@type="submit"]').click()
            sleep(3)


    def SearchUser(self):
        pass


bot = Instagram()
bot.Open_Browser()
sleep(3)
# bot.Like_comment_Hashtag()
