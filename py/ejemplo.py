from pickle import TRUE
import sys


y=1

while TRUE:
    try:
        a=input("Introduzca un numerador: ")
        b=input("Introduzca el denominador: ")
        d= a/b
    except KeyboardInterrupt as e:
        print ("\n[*] Apagando...")
        raise
    except:
        print("/n El numerador no se puede dividir entre 0 /n")