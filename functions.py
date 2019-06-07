import sys
import os
import os.path as osp
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://github.com/login')

def login(username_, password_):
    try:
        python_button = browser.find_elements_by_xpath(
            "//input[@name='login']")[0]
        python_button.send_keys(username_)

        python_button = browser.find_elements_by_xpath(
            "//input[@name='password']")[0]
        python_button.send_keys(password_)

        python_button = browser.find_elements_by_xpath(
            "//input[@name='commit']")[0]
        python_button.click()

        if(browser.find_elements_by_xpath('//*[@id="js-flash-container"]/div/div')[0]):
            browser.quit()
            return 2
    except:
        print("\n\nUsuário: {} Logado!\n\n".format(username_))
        return 1

def delfolder(reponame_):
    os.system("rm -Rf " + reponame_)

def verificarepo(reponame_):
    browser.get('https://github.com/silv4b?tab=repositories')

    python_button = browser.find_elements_by_xpath('//*[@id="your-repos-filter"]')[0]
    python_button.send_keys(reponame_)

    if(browser.find_elements_by_xpath('//*[@id="user-repositories-list"]/div[1]/div[1]')):
        #print("Repositório não existe!")
        browser.quit()
        return 1

def remove(reponame_):

    if(verificarepo(reponame_) != 1):    
        browser.get('https://github.com/silv4b/' + reponame_ + '/settings')        

        python_button = browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0]
        python_button.click()

        python_button = browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0]
        python_button.send_keys(reponame_)

        python_button = browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0]
        python_button.click()

        browser.quit()

        delfolder(reponame_)

        return
    else:
        return 1   

def createoffline (reponame_):
    print("---> Criar pasta.")
    if os.path.isdir(reponame_):
        print("------>Pasta já existe offline\n------>Cancelar!")
        browser.quit()
        return 1
    else:
        os.system("mkdir " + reponame_)
        print("---> Pasta criada")

    print("---> Into the folder: ", end="")
    path = os.getcwd()
    path = path + '/' + reponame_ + '/'
    os.chdir(path)
    print(path + '\n')

    # cria o readme.md
    os.system("echo 'readme' >> readme.md")

    # inicializa o repositório
    os.system("git init")
    os.system("git add .")
    os.system("git status")

    #mensagem
    print("---> Repositório criado offline")

def createonline (username_, password_, reponame_):
    browser.get('https://github.com/new')

    try:
        python_button = browser.find_elements_by_xpath("//input[@name='repository[name]']")[0]
        python_button.send_keys(reponame_)

        python_button = browser.find_element_by_css_selector('button.first-in-line')
        # //*[@id="new_repository"]/div[2]/auto-check/dl/dd[2]
        if(browser.find_elements_by_xpath('/*[@id="new_repository"]/div[2]/auto-check/dl/dd[2]')):
            print("repositório já existe!")
            browser.quit()
            return
        else:
            python_button.submit()
    except:
        print("SEILA")

def ligaremoto(username_, reponame_):
    os.system("git commit -m 'initial commit'")
    #os.system("git remote add origin git@github.com:" + username_ + "/" + reponame_ + ".git")
    # git remote add origin git@github.com:silv4b/123.git
    os.system("git remote add origin git@github.com:{}/{}.git".format(username_, reponame_))
    os.system("git push -u origin master")
    browser.get("http://github.com/" + username_ + "/" + reponame_)
