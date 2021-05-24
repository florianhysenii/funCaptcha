from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome()
driver.get("https://www.myprepaidcenter.com/login/card")
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/app-root/app-shell/app-card-login-page/div/form/div/div/div/app-card-information/form/div[1]/div/div/input")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-shell/app-card-login-page/div/form/div/div/div/app-card-information/form/div[1]/div/div/input "))).send_keys("1234567890987654")