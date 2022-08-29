from selenium import webdriver
from time import sleep
from details import username,password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

hashtag = ['python', 'javascript', 'React']

class Instagram():
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    
    def Open_Browser(self):
        self.driver.get('https://www.instagram.com/')
        self.driver.implicitly_wait(5)
        self.login()
    
    
    def login(self):
        login_block = self.driver.find_element(By.XPATH, '//input[@name = "username"]')
        password_block = self.driver.find_element('xpath', '//input[@name="password"]')
        
        login_block.send_keys(username)
        password_block.send_keys(password)
        password_block.send_keys(Keys.ENTER)
        
        save_no_info = self.driver.find_element('xpath', '/html/body/div[1]/section/main/div/div/div/div/button').click()
        no_notification = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        
    def Like_comment_Hashtag(self):
       self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag[random.randint(0,3)]))
       links = self.driver.find_elements_by_tag_name('a')
       print(links)


bot = Instagram()
bot.Open_Browser()
sleep(3)
bot.Like_comment_Hashtag()
