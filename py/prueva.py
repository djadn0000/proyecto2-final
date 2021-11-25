from os import error
import socket
from py.proxyServer import proxy_server
import request
import sys
from thread import *

def main():
    port =2021
    buffer_size = 8192
    max_conn=100
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind('',port)
        server.listen(max_conn)
        print("[*] Inicializando socket... hecho.")
        print("[*] Socket atado exitosamente...")
        print("[*] El servidor inicio exitosamente [{}]".format(port))
    except Exception as e:
        print (e)
        sys.exit(2)
    while True:
        try:
            coneccion, direccion =server.accept()
            data= coneccion.recv(buffer_size)
        except Exception as e:
            print(e)
            sys.exit(1)
    server.close()

def conn_strinng(conn, data, addr):

    try:
        
        primera_linea=data.split("\n")[0]
        url= primera_linea.split(" ")[1]
        print("{},{}".format(data[0],data[1]))

        http_post = url.find("://")
        if http_post == -1:
            tem=url
        else:
            tem= url[(http_post + 3):]
       
        port_post= tem.fin(":")

        webserver_post = tem.find("/")
        
        if webserver_post == -1:
            webserver_post = len(tem)
        webserver= ""
        port = -1

        if port_post == -1 or webserver_post < port_post:
            puerto = 80
            webserver = tem[:webserver_post]
        else:
            puerto= int(tem[(port_post)])
            webserver = tem[:port_post]
        
        print(webserver)
        proxy_server(webserver, puerto, conn, addr)
    except Exception as e:
        print(e)

def proxy_server(webserver,port,conn, data, addr):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((webserver,port))
        server.send(data)

        while True:
            reply = server.recv(buffer_size)

            if len(reply) > 0:
                conn.send(reply)

                dar =float(len(reply))
                dar=float(dar/1024)
                dar ="{}.3s".format(dar)
                print ("[*] El pedido esta hecho: {} => {} <= {}".format(addr[0], dar, webserver))
            else:
                break
            server.close()
            conn.close()
    except socket.error (value, msg):
        server.close()
        conn.close()
        sys.exit(1)



if __name__=="__main__":
    main()

        
