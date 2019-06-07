import sys
import os
import functions as func

username = sys.argv[1]
password = sys.argv[2]
reponame = sys.argv[3]
action = sys.argv[4]

return_ = func.login(username, password)

if(return_ == 1):
    if(action == "-c"):
        if (func.createoffline(reponame) == 1):
            print("Pasta já existe")
            sys.exit()
        func.createonline(username, password, reponame)
        func.ligaremoto(username, reponame)
    elif(action == "-d"):
        if (func.remove(reponame) == 1):
            print("Repositório não existe! CANCELADO")
            sys.exit()
elif(return_ == 2):
    print("[ERRO AO LOGAR]")
