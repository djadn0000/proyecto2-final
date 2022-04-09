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


import hashlib
import json
from pickle import TRUE
from numpy import append
import requests
import urllib
import csv
Extendicc = {'extention': ['exe', 'jpg', 'png', 'dll', 'bat', 'bin',
                           'txt', 'doc', 'exec', 'ptt', 'py', 'mp3', 'mp4', 'application']}


def FileExtenxion(link):
    r = requests.get(link)
    dicc = dict(r.headers)
    #print('{} \n\n'.format(dicc))
    if 'Content-Disposition' in dicc:
        res = dicc["Content-Disposition"]
        sp = res.split('.')
        t = sp[-1].strip('"')
    elif 'Content-Type' in dicc:
        res = dicc["Content-Type"]
        sp = res.split('/')
        t = sp[0]
    elif 'content-disposition' in dicc:
        res = dicc["content-disposition"]
        sp = res.split('.')
        t = sp[-1].strip('"')
    else:
        t = 'no exiten'
    return t

# print(FileExtenxion('https://get.videolan.org/vlc/3.0.16/win32/vlc-3.0.16-win32.exe'))


def FileExtencionByUrl(link):
    st = link.split('/')
    sst = st[-1]
    tst = sst.split('.')
    solu = tst[-1]
    return solu


# print(FileExtencionByUrl('https://download2325.mediafire.com/1cpazj2jyvcg/kmn6o5kwjkqnbex/Ms+Office+2021+Pro+LTSC+-+ACTUALIZADO.rar'))

def DownloadFile(link):

    try:
        st = link.split('/')
        sst = st[-1]
        file = sst
        st = link.split('/')
        sst = st[-1]
        file = sst

        r = urllib.request.urlopen(link)
        f = open('cuarentena/' + file, 'wb')
        f.write(r.read())
        f.close()

    except Exception as e:
        print('No hay aplicacion que descargar')

# DownloadFile('http://misiontokyo.com/wp-content/uploads/2021/10/Detec1-770x838.jpg')


def AskToDownload(link):
    a = FileExtenxion(link)
    b = FileExtencionByUrl(link)

    if a in Extendicc['extention'] or b in Extendicc['extention']:
        DownloadFile(link)
        return TRUE


# AskToDownload('http://misiontokyo.com/wp-content/uploads/2021/10/Detec1-770x838.jpg')


def InsertToList(name, md5):
    f = open("dicc.json", "r")
    c = f.read()
    f.close()
    js = json.loads(c)
    js["Name"].append(name)
    js["md5"].append(md5)
    s = json.dumps(js, indent=4)
    w = open("dicc.json", "w")
    w.write(s)


def CsvTodic():
    with open('data.csv', mode='r') as infile:
        reader = csv.DictReader(infile, delimiter='|')

        count = 0
        for row in reader:

            InsertToList(row['Name'], row['md5'])
            print("name: {}, Md5: {}".format(row['Name'], row['md5']))

            ''' if count > 5:
                break
            count += 1'''


'''
        with open ('coor_new.csv', mode='w') as outfile:
            writer= csv.writer(outfile)
            mydict= {rows[0]:rows[1] for rows in reader} 
    print(mydict)     '''

# CsvTodic()


def AddNew(name):
    f = open("dicc.json", "r")
    c = f.read()
    f.close()
    js = json.loads(c)
    if name in js['Name']:
        print('si se pudo encontrar')
    else:
        print('no se pudo encontrar')
# prueba("3bc20b8cf096f7d19b0236e934866098")


def FileaToMd5(file):

    path = r'/var/www/html/proyecto2-final/py/cuarentena/{}'.format(file)
    with open(path, 'rb') as newfile:
        content = newfile.read()
        md5 = hashlib.md5()
        md5.update(content)
        s = md5.hexdigest()

        print('El Md5 del Archivo: {} es:  {}'.format(file, s))

        return md5.hexdigest()

# FileaToMd5('AnyDesk.exe')


def DownloadAndCheckRamson(link):
    if AskToDownload(link):
        try:
            st = link.split('/')
            sst = st[-1]
            file = sst
            st = link.split('/')
            sst = st[-1]
            file = sst
        
            f = open("dicc.json", "r")
            c = f.read()
            f.close()
            js = json.loads(c)

            md5 = FileaToMd5(file)

            if md5 in js['md5']:
                return b'proyectoadrianitt.ddns.net'



            
        except Exception as e:
            print('No hay aplicacion que descargar')
