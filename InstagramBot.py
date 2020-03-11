from selenium import webdriver
from time import sleep

class InstaFollowersBot:

    def __init__(self, username):
        url = "https://instagram.com/" + username
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        sleep(1)

    def get_info(self):
        followers_element = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span'
        posts_element = '/html/body/div[1]/section/main/div/header/section/ul/li[1]'

        followers = self.driver.find_element_by_xpath(followers_element).get_attribute("title")
        posts = self.driver.find_element_by_xpath(posts_element).text
        
        posts = posts.replace(' posts', '')
        posts = int(posts.replace(',', ''))
        followers = int(followers.replace(',', ''))
        
        self.driver.quit()
        result = [followers, posts]
        return(result)

print(InstaFollowersBot('instagram_handle').get_info())
