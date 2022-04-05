'''from pickle import TRUE
import sys


y=1

while TRUE:
    try:
        a=input("Introduzca un numerador: ")
        b=input("Introduzca el denominador: ")
        d= a/b
    except KeyboardInterrupt as e:
        print ("\n[*] Apagando...")
        
    except:
        print("/n El numerador no se puede dividir entre 0 /n")'''


import json
import requests

def FileExtenxion(link):
    r = requests.get(link)
    dicc=dict(r.headers)
    print('{} \n\n'.format(dicc))
    if  'Content-Disposition' in dicc:
        res=  dicc["Content-Disposition"]
        sp = res.split('.')
        t = sp[-1].strip('"')
    elif 'Content-Type' in dicc :
        res=  dicc["Content-Type"]
        sp = res.split('/')
        t = sp[0]
    elif  'content-disposition' in dicc:
        res=  dicc["content-disposition"]
        sp = res.split('.')
        t = sp[-1].strip('"')
    else:
        t='no exiten'
    return t 

print(FileExtenxion('https://get.videolan.org/vlc/3.0.16/win32/vlc-3.0.16-win32.exe'))


def FileExtencionByUrl(link):
    st  = link.split('/')
    sst = st[-1]
    tst = sst.split('.')
    solu = tst[-1]
    return solu
    

print(FileExtencionByUrl('https://download2325.mediafire.com/1cpazj2jyvcg/kmn6o5kwjkqnbex/Ms+Office+2021+Pro+LTSC+-+ACTUALIZADO.rar'))