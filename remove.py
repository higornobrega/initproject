import sys
import os
from selenium import webdriver

username = sys.argv[1]
password = sys.argv[2]
reponame = sys.argv[3]

browser = webdriver.Chrome()
browser.get('http://github.com/login')


def delfolder():
    os.system("rm -Rf " + reponame)


def remove():
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='password']")[0]
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/silv4b/' + reponame + '/settings')

    python_button = browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0]
    python_button.click()
    python_button = browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0]
    python_button.send_keys(reponame)

    python_button = browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0]
    python_button.click()

    #browser.get("https://github.com/" + username)
    browser.quit()


if __name__ == "__main__":
    remove()
    delfolder()
