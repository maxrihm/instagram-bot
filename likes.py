from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import datetime
start_time = time.time()
session_likes = 0
total_likes = 0
users_liked = []
path = "InstagramBot\\chromedriver.exe"
hashtags = "InstagramBot\\hashtags.txt"
browser = webdriver.Chrome(path)
def login(username, password):
    print(f'Login phase')
    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(3, 5))
    username_input = browser.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys(username)
    time.sleep(random.randrange(3, 5))
    password_input = browser.find_element_by_name('password')
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(random.randrange(3, 5))
    password_input.send_keys(Keys.ENTER)
    time.sleep(random.randrange(8, 10))
def hashtag_search(hashtag):
    try:
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
        time.sleep(random.randrange(8, 10))
        List_first_photo = browser.find_elements_by_xpath("//a[@href]")
        List_real_first_photo = []
        for elem in List_first_photo:
            List_real_first_photo.append(elem.get_attribute("href"))
        element_link = List_real_first_photo[9]
        element_link = "/p/" + element_link.split("/")[4] + "/"
        browser.find_element_by_xpath('//a[@href="' + element_link + '"]').click()
        print('Open first recent photo')
        print('Session start')
        try:
            likes_count = 0
            skips = 0
            skips_limit = 6
            global session_likes
            global total_likes
            global likes_limit
            global users_liked
            while likes_count < 50:
                try:
                    skips = 0
                    time.sleep(random.randrange(3, 5))
                    try:
                        List = browser.find_elements_by_xpath("//a[@href]")
                        List_real = []
                        for elem in List:
                            List_real.append(elem.get_attribute("href"))
                        index = List_real.index("https://www.instagram.com/web/lite/")
                        username = List_real[index + 1]
                        username = username.rsplit('/', 2)
                        username = username[1]
                        print(f'We are currently on post by {username}')
                    except Exception as ex:
                        print(f'There is something wrong with the current post. Next photo -->')
                        time.sleep(random.randrange(3, 5))
                        press_right = browser.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
                        time.sleep(random.randrange(3, 5))
                        List = browser.find_elements_by_xpath("//a[@href]")
                        List_real = []
                        for elem in List:
                            List_real.append(elem.get_attribute("href"))
                        index = List_real.index("https://www.instagram.com/web/lite/")
                        username = List_real[index + 1]
                        username = username.rsplit('/', 2)
                        username = username[1]
                        print(f'We are currently on post by {username}')
                    if skips <= skips_limit and total_likes <= likes_limit:
                        if username not in users_liked:
                            if browser.find_elements_by_css_selector("button span > svg[aria-label='Unlike']"):
                                print(f'The post has already been liked. Next photo -->')
                                skips += 1
                            else:
                                time.sleep(random.randrange(40, 60))
                                press_like = browser.find_element_by_css_selector(
                                    "button span > svg[aria-label='Like']").click()
                                likes_count += 1
                                total_likes += 1
                                users_liked.append(username)
                                print(f'Like! Photos liked: {likes_count}, user: {username}')
                                session_likes = likes_count
                                time.sleep(random.randrange(20, 30))
                        else:
                            print(f'We already liked this user in current session. Next photo -->')
                        try:
                            time.sleep(random.randrange(3, 5))
                            press_right = browser.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
                        except Exception as ex:
                            print(ex)
                    else:
                        print(f'Too many liked photos in the feed or we hit likes limit (X) Stopping a session')
                        break
                except Exception as ex:
                    print(ex)
            browser.get('https://www.instagram.com')
        except Exception as ex:
            print(ex)
    except Exception as ex:
        print(ex)
hashtag_list = open(hashtags).read().splitlines()
random.shuffle(hashtag_list)
likes_limit = 250
login('username here', 'password here')
for current_hashtag in hashtag_list:
    if total_likes <= likes_limit:
        print(f'Bot starts session with #{current_hashtag}')
        session_likes = 0
        start = time.time()
        hashtag_search(current_hashtag)
        idle_time = random.randrange(1200, 1800)
        idle_time_converted = datetime.timedelta(seconds=idle_time)
        print(
            f'The whole session took: {datetime.timedelta(seconds=int(time.time() - start))}, and we placed {session_likes} :heart: Now idle for {idle_time_converted}. Total likes: {total_likes}')
        time.sleep(idle_time)
    else:
        browser.close()
        browser.quit()
        break
workedTime = str(int((time.time() - start_time)))
with open('InstagramBot\\time.txt', 'w') as f:
    f.write(workedTime)
