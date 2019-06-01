import sys
from selenium import webdriver

username = sys.argv[1]
password = sys.argv[2]
reponame = sys.argv[3]

browser = webdriver.Chrome()
browser.get('http://github.com/login')


def create():
    python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
    python_button.send_keys(username)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='password']")[0]
    python_button.send_keys(password)
    python_button = browser.find_elements_by_xpath(
        "//input[@name='commit']")[0]
    python_button.click()
    browser.get('https://github.com/new')
    python_button = browser.find_elements_by_xpath(
        "//input[@name='repository[name]']")[0]
    python_button.send_keys(reponame)
    python_button = browser.find_element_by_css_selector(
        'button.first-in-line')
    python_button.submit()


if __name__ == "__main__":
    create()
