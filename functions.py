import sys
import os
import os.path as osp
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('http://github.com/login')

# coloque o caminho da pasta onde irá guardar seus projetos
caminho = '/home/bruno/Documentos/Testes/'

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
        return 1


def verificarepo(reponame_):
    browser.get('https://github.com/silv4b/' + reponame_ + '/settings')
    try:
        if(browser.find_elements_by_xpath('/html/body/div[4]/main/div[1]/div[2]/img[1]')[0]):
            print("Função: verificarepo(reponame_)")
            print("\tRepositório não existe!")
            return False # se não existir
    except:
        if(browser.find_elements_by_xpath('//*[@id="options_bucket"]')[0]):
            print("Função: verificarepo(reponame_)")
            print("\tRepositório existe!")
            return True # se existir

def delfolder(reponame_):
    reponame_ = caminho + reponame_
    print("\n\t {} ".format(reponame_))

    if os.path.isdir(reponame_):
        print("------>Pasta existe offline\n------>Excluir!")
        print("---> Into the folder: ", end="")
        path = reponame_
        os.chdir(path)
        os.system("rm -Rf " + reponame_)

def remove(reponame_):
    if(verificarepo(reponame_) == True):
        browser.get('https://github.com/silv4b/' + reponame_ + '/settings')

        python_button = browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0]
        python_button.click()

        python_button = browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0]
        python_button.send_keys(reponame_)

        python_button = browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0]
        python_button.click()

        delfolder(reponame_)
        browser.quit()

        return True # excluiu do github
    else:
        return False # repositório  não existe

def createoffline (reponame_):
    print("---> Criar pasta.")

    reponame_ = caminho + reponame_
    print("\n\t {} ".format(reponame_))

    if os.path.isdir(reponame_):
        print("------>Pasta já existe offline\n------>Cancelar!")
        browser.quit()
        return 1
    else:
        os.system("mkdir " + reponame_)
        print("---> Pasta criada")

    print("---> Into the folder: ", end="")
    path = reponame_
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
    os.system("git remote add origin git@github.com:{}/{}.git".format(username_, reponame_))
    os.system("git push -u origin master")
    browser.get("http://github.com/" + username_ + "/" + reponame_)
