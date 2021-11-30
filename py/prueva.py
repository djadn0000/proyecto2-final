import socket
import sys 
from thread import *




def main():
    global listen_port, buffer_size, max_conn
    try:
        #preguntar por el puerto donde se esta ejecutando el servidor
        listen_port= 3128
    except KeyboardInterrupt:
        sys.exit(0)
        
    max_conn = 100
    buffer_size =8192
    #
    try:
        #inicializando los sockets, resive el request de los clientes y inicia un hilo para devolver el pedido
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', listen_port))
        s.listen(max_conn)
        print("[*] Inicializando socket... hecho.")
        print("[*] Socket atado exitosamente...")
        print("[*] El servidor inicio exitosamente [{}]".format(listen_port))
    except Exception as e:
        print(e)
        sys.exit(2)
        
        
    while True:
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)  
            start_new_thread(conn_string, (conn, data, addr))           
                
        except KeyboardInterrupt:
            s.close()
            print ("\n[*] Apagando...")
            sys.exit(1)
            
    s.close()
# esta funcion em devuelve la diereccion del host comunica al buscador  
def conn_string(conn, data, addr):
    try:
        
        first_line = data.split("\n")[0]
        url= first_line.split(" ")[1]
        
        print("###########################################")
        print(data)
        print("###########################################")
        print(r.json)
        print("###########################################")        
        
        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]

        port_pos = temp.find(":")
        
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos =len(temp)
        webserver = ""
        port = -1
        
        if port_pos == -1 or webserver_pos < port_pos:
             port = 80
             webserver= temp[:webserver_pos]
        else:
            port= int(temp[(port_pos + 1 ):][:webserver_pos - port_pos -1])
            webserver = temp[:port_pos]
        
        
        print(webserver)
        proxy_server(webserver, port, conn, data, addr)
    except Exception as e:
        print(e)

 #crea un socket nuevo, se connecta al web server y envia el request al cliente  
def proxy_server(webserver, port, conn, data, addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(data)

        while True:
            reply = s.recv(buffer_size)
            
            if len(reply) > 0:
                conn.send(reply)

                dar = float(len(reply))
                dar = float(dar/1024)
                dar = "{}.3s".format(dar)
              # print ("[*] El pedido esta hecho: {} => {} <= {}".format(addr[0], dar, webserver))
            else:
                break
            
        s.close()
        conn.close()
    except socket.error (value, msg):
        s.close()
        conn.close()
        sys.exit(1)
        
if __name__ == "__main__":
    main()
