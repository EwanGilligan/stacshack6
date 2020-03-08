from selenium import webdriver
import selenium.webdriver.support.ui as ui
from time import sleep
from selenium.webdriver.common.by import By
from getpass import getpass
import json


# with open("../config.json") as f:
#     json_file = json.load(f)
#
# username = json_file["username"]
# password = json_file["password"]
def get_contents(urls, heading_file, paragraph_file, speach_part):
    driver = webdriver.Firefox()
    driver.get("https://www.dndbeyond.com/login")
    # driver.find_element_by_id("signin-with-twitch").click()
    # driver.find_element_by_id("login-username").send_keys(username)
    # driver.find_element_by_id("password-input").send_keys(password)
    # sleep(1)
    # driver.find_element_by_class_name("tw-core-button-label").click()
    with open(heading_file, "w+") as f_head, open(paragraph_file, "w+") as f_para, open(speach_part, "w+") as f_speach:
        wait = ui.WebDriverWait(driver, 60)
        wait.until(lambda d: d.find_elements_by_class_name("site-bar"))
        for url in urls:
            driver.get(url)
            sleep(1)
            headings = driver.find_elements_by_class_name("compendium-hr")
            for heading in headings:
                f_head.write(heading.text + "\n")
            paragraphs = driver.find_elements_by_xpath("//p")
            for paragraph in paragraphs:
                f_para.write(paragraph.text)
            spoken_parts = driver.find_elements_by_class_name("adventure-read-aloud-text")
            for spoken_part in spoken_parts:
                f_speach.write(spoken_part.text)
            sleep(10)


with open("../data/links1.txt") as f:
    lines = f.readlines()

get_contents(lines, "../data/headingsFull.txt", "../data/paragraphsFull.txt", "../data/spokenFull.txt")
