import sys
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://github.com/login')


def create_(username_, password_, reponame_):
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username_)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='password']")[0]
    python_button.send_keys(password_)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath(
        "//input[@name='repository[name]']")[0]
    python_button.send_keys(reponame_)
    python_button = browser.find_element_by_css_selector(
        'button.first-in-line')
    python_button.submit()


def reload_(reponame_):
    browser.get('https://github.com/silv4b/' + reponame_)
