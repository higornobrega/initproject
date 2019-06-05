import sys
import os
import create as c

username = sys.argv[1]
password = sys.argv[2]
namefolder = sys.argv[3]

# cria diretório
mkdir = "mkdir "
cmdmkdir = mkdir + namefolder
os.system(cmdmkdir)

# navega até o diretório
path = os.getcwd()
path = path + '/' + namefolder + '/'
os.chdir(path)

# cria o readme.md
os.system("echo 'readme' >> readme.md")

# passos do git [1/2]
print("-"*15)
os.system("git init")
os.system("git add .")
os.system("git status")
print("-"*15)

# subpasso cria repositório
return_ = c.create_(username, password, namefolder)

if (return_ == 1):
    print("RETORNOU 1, ABORTADO!")
else:
    # CRIAR
    # passos do git [2/2]
    print("-"*15)
    os.system("git commit -m 'initial commit'")
    os.system("git remote add origin git@github.com:silv4b/" +
              namefolder + ".git")
    os.system("git push -u origin master")
    print("-"*15)

    c.reload_(namefolder)
