from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
from details import username,password
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
        
    # the below code is not working , Should try finding new approach
        
    def Messaging(self):
        mssg_btn = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        links = self.MessgPeople()
        print(links)
    
    
    def MessgPeople(self):
        frnds_profile = self.driver.find_element('class name', '_abyk')
        name_link_lst = []
        for profile in frnds_profile:
            name_link_lst.append(profile.get_attribute('href'))
        return name_link_lst
    
    
    def Post(self):
        post_btn = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
        
        select_btn = self.driver.find_element('xpath', '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()
        

bot = Instagram()
bot.Open_Browser()
sleep(3)
# bot.Messaging()
bot.Post()
