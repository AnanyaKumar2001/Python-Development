# **************-------------------- Automating The Browser
from selenium import webdriver
import time

# opening the browser
browser = webdriver.Firefox()
browser.get("https://gmail.com")

# username
username_field = browser.find_element_by_id("identifierId")
username_field.send_keys("pythond63@gmail.com")

# clicking the next button
next_btn = browser.find_element_by_class_name("VfPpkd-RLmnJb")
next_btn.click()

time.sleep(5)

password_field = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
password_field.send_keys("hey2100there")

# clicking the next button
next_btn = browser.find_element_by_class_name("VfPpkd-RLmnJb")
next_btn.click()
