from instagramUserinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException

import unittest, time, re,datetime,os,sys

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password


    def SingIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

        
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(3)
        
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count : {followerCount}")

        action = webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()
            action.send_keys(Keys.SPACE).send_keys(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(2)
            else:       
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)

    def followUser(self, username):
        self.browser.get("httos://www.instagram.com/"+ username)
        time.sleep(2)

        followbutton = self.browser.find_element_by_tag_name("button")
        print(followbutton.text)

instgrm = Instagram(username, password)
instgrm.SingIn()
# instgrm.getFollowers()
instgrm.followUser("celenk.o")