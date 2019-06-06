import sys
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)  # seconds
if (browser.get('http://github.com/login')):
    print("Carregou")



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

    if (browser.find_elements_by_xpath('//*[@id="new_repository"]/div[2]/auto-check/dl/dd[2]')[0]):
        print("REPOSITÓRIO JÁ EXISTE!")
        browser.quit()
        return 1
    else:
        python_button = browser.find_element_by_css_selector(
            'button.first-in-line')
        python_button.submit()
    return 0

    browser.get('https://github.com/' + username_ + '/' + reponame_)


def reload_(username_, reponame_):
    browser.get('https://github.com/' + username_ + '/' + reponame_)
