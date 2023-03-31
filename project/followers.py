from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import requests
import os
import json


class InstagramBot():
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("InstagramBot\\chromedriver.exe")

    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    def login(self):

        browser = self.browser
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(5, 7))

        username_input = browser.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(random.randrange(3, 5))

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(random.randrange(3, 5))

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(10, 20))

    def smart_unsubscribe(self, username):

        browser = self.browser
        browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(random.randrange(6, 10))

        followers_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
        followers_count = followers_button.get_attribute("title")

        following_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following_count = following_button.find_element_by_tag_name("span").text

        time.sleep(random.randrange(5, 8))

        if ',' in followers_count or following_count:
            followers_count, following_count = int(''.join(followers_count.split(','))), int(''.join(following_count.split(',')))
        else:
            followers_count, following_count = int(followers_count), int(following_count)

        print(f"Subscribers count: {followers_count}")
        followers_loops_count = int(followers_count / 12) + 1
        print(f"Iterations to get subscribers: {followers_loops_count}")

        print(f"Following count: {following_count}")
        following_loops_count = int(following_count / 12) + 1
        print(f"Iterations to get subscribers: {following_loops_count}")

        # собираем список подписчиков
        followers_button.click()
        time.sleep(4)

        followers_ul = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]")

        try:
            followers_urls = []
            print("Gethering subscribers...")
            for i in range(1, followers_loops_count + 1):
                browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_ul)
                time.sleep(random.randrange(2, 4))
                print(f"Iteration #{i}")

            all_urls_div = followers_ul.find_elements_by_tag_name("li")

            for url in all_urls_div:
                url = url.find_element_by_tag_name("a").get_attribute("href")
                followers_urls.append(url)

            open('account_followers_list.txt', 'w').close()
            with open(f"{username}_followers_list.txt", "a") as followers_file:
                for link in followers_urls:
                    followers_file.write(link + "\n")
        except Exception as ex:
            print(ex)
            self.close_browser()

        time.sleep(random.randrange(4, 6))
        browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(random.randrange(3, 6))

        following_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following_button.click()
        time.sleep(random.randrange(3, 5))

        following_ul = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")

        try:
            following_urls = []
            print("Start subscription gather...")

            for i in range(1, following_loops_count + 1):
                browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_ul)
                time.sleep(random.randrange(2, 4))
                print(f"Iteration #{i}")

            all_urls_div = following_ul.find_elements_by_tag_name("li")

            for url in all_urls_div:
                url = url.find_element_by_tag_name("a").get_attribute("href")
                following_urls.append(url)

            open('account_following_list.txt', 'w').close()
            with open(f"{username}_following_list.txt", "a") as following_file:
                for link in following_urls:
                    following_file.write(link + "\n")

            favorite_list = []
            with open("account_favorite_list.txt") as f:
                favorite_list = sorted(word.strip(",") for line in f for word in line.split())

            count = 0
            unfollow_list = []
            for user in following_urls:
                if (user not in followers_urls) and (user not in favorite_list):
                    count += 1
                    unfollow_list.append(user)
            print(f"We have to unfollow from {count} users")
            print(unfollow_list)
            open('account_unfollow_list.txt', 'w').close()
            with open(f"{username}_unfollow_list.txt", "a") as unfollow_file:
                for user in unfollow_list:
                    unfollow_file.write(user + "\n")
            if unfollow_list:
                action_unsibscribe = input("Unsubscribe from users above? [y/n]: ")
                if (action_unsibscribe=='y'):
                    print("Start unsubscribtion...")
                    time.sleep(2)

                    with open(f"{username}_unfollow_list.txt") as unfollow_file:
                        unfollow_users_list = unfollow_file.readlines()
                        unfollow_users_list = [row.strip() for row in unfollow_users_list]

                    try:
                        count = len(unfollow_users_list)
                        for user_url in unfollow_users_list:
                            browser.get(user_url)
                            time.sleep(random.randrange(15, 30))

                            unfollow_button = browser.find_element_by_xpath('//span[@aria-label="Following"]')
                            unfollow_button.click()

                            time.sleep(random.randrange(8, 16))

                            unfollow_button_confirm = browser.find_element_by_xpath('//button[text()="Unfollow"]')
                            unfollow_button_confirm.click()

                            print(f"Unsubscribed from {user_url}")
                            count -= 1
                            print(f"It remains to unsubscribe from: {count} users")

                            # time.sleep(random.randrange(120, 130))
                            time.sleep(random.randrange(20, 40))
                    except Exception as ex:
                        print(ex)
                        self.close_browser()
        except Exception as ex:
            print(ex)
            self.close_browser()
        else:
            time.sleep(random.randrange(4, 6))
            self.close_browser()


username = 'username here'
password = 'password here'
my_bot = InstagramBot(username, password)
my_bot.login()
my_bot.smart_unsubscribe('account')
