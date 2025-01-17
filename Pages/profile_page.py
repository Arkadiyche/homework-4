from Pages.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time

class ProfilePage(Page):
    PATH = '/profile'
    PLAYLIST = '//a[@id="play"]'
    PLAYLIST_INPUT = '//input[@class="name__input_main--1fQSy"]'
    PLAYLIST_BUTTON = '//button[text()="Создать"]'
    PLAYLIST_NAME = '//div[@class="name__filmlenta_genre--2DRas"]'
    PLAYLIST_DELETE = '//div[@class="name__delete--2d58m"]'
    FILM_DELETE = '//div[@class="name__delete--2d58m"][contains(@id, "poster")]'
    FILM_IN_PLAYLIST = '//div[@class="name__lenta__object--3-XkZ"]/a[@id="1"]'
    FILMS_IN_PLAYLIST = '//div[@class="name__lenta__object--3-XkZ"]'
    SUBSCRIBERS = '//a[@id="subscribe"]'
    ENTRY = '//button[text()="Войти"]'
    USERNAME = '//span[@class="name__profile__default_margin--_Vkp5 name__profile_login--2W71f"]'
    DELETE_USER = '//button[@id="deleteProfile"]'
    FRIEND = '//a[@href="people/17"]'

    def open_subscribers(self):
        self.open()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.SUBSCRIBERS)))
        self.driver.find_element_by_xpath(self.SUBSCRIBERS).click()

    def open_playlist(self):
        self.open()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.PLAYLIST)))
        self.driver.find_element_by_xpath(self.PLAYLIST).click()

    def set_playlist(self, new):
        self.driver.find_element_by_xpath(self.PLAYLIST_INPUT).send_keys(new)

    def submit_playlist(self):
        self.driver.find_element_by_xpath(self.PLAYLIST_BUTTON).click()

    def wait_playlist_create(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.PLAYLIST_NAME)))

    def wait_playlist_delete(self):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.PLAYLIST_NAME)))

    def wait_film_add(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.FILM_IN_PLAYLIST)))

    def wait_film_delete(self):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, self.FILM_IN_PLAYLIST)))

    def check_playlist(self, playlist):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.PLAYLIST_NAME)))
        name = self.driver.find_element_by_xpath(self.PLAYLIST_NAME).text
        if name == playlist:
            return True
        else:
            return False

    def check_film_in_playlist(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.FILM_IN_PLAYLIST)))
        self.driver.find_element_by_xpath(self.FILM_IN_PLAYLIST)

    def get_count_playlist(self):
        try:
            count = len(self.driver.find_elements_by_xpath(self.PLAYLIST_NAME))
        except NoSuchElementException:
            return 0
        else:
            return count

    def get_count_film_in_playlist(self):
        try:
            count = len(self.driver.find_elements_by_xpath(self.FILMS_IN_PLAYLIST))
        except NoSuchElementException:
            return 0
        else:
            return count - 1

    def delete_playlist(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.PLAYLIST_DELETE)))
        self.driver.find_element_by_xpath(self.PLAYLIST_DELETE).click()

    def delete_film_from_playlist(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.FILM_DELETE)))
        self.driver.find_element_by_xpath(self.FILM_DELETE).click()

    def create_playlist(self, name):
        self.open_playlist()
        self.set_playlist(name)
        self.submit_playlist()

    def get_friend_login(self):
        self.open_subscribers()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.FRIEND)))
        return self.driver.find_element_by_xpath(self.FRIEND).text

    def check_unsub(self, path):
        self.open_subscribers()
        friend = '//a[@href="' + path + '"]'
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, friend)))

    def unsub(self, path):
        self.open_subscribers()
        delete = '//div[@id="' + path + '"]'
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, delete)))
        self.driver.find_element_by_xpath(delete).click()
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.XPATH, delete)))
        
    def check_username(self, username):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        username_in_profile = self.driver.find_element_by_xpath(self.USERNAME).text
        if username_in_profile == username:
            return True
        else:
            return False

    def get_username(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.USERNAME)))
        return self.driver.find_element_by_xpath(self.USERNAME).text

    def delete_user(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.DELETE_USER)))
        self.driver.find_element_by_xpath(self.DELETE_USER).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ENTRY)))
