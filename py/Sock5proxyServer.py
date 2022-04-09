from distutils import extension
from hashlib import md5
from importlib.resources import contents
from pprint import pprint
from pydoc import doc
import socket
import threading
import select
import sys
import dbconf
import json
import requests
import urllib
from asyncore import write


SOCKS_VERSION = 5
database = dbconf.DataBase()
global Extendicc, host_path,virusDicc

host_path = "/etc/hosts"
Extendicc = {'extention': ['exe', 'jpg', 'png', 'dll', 'bat', 'bin', 'txt','doc', 'exec', 'ptt', 'py', 'mp3', 'mp4', 'msi', 'image', 'application']}

class Proxy:
    def __init__(self):

        self.username = "username"
        self.password = "password"
         

    # download the file to scan
    def DownloadFile(self, link):

        try:
            st = link.split('/')
            sst = st[-1]
            file = sst
            st = link.split('/')
            sst = st[-1]
            file = sst

            r = urllib.request.urlopen(link)
            f = open('virus_detector/cuarentena/' + file, 'wb')
            f.write(r.read())
            f.close()

                    
        except Exception as e:
            print('No hay aplicacion que descargar')

    # file extension extractor by domin name
    def FileExtencionByUrl(self, link):
        st = link.split('/')
        sst = st[-1]
        tst = sst.split('.')
        solu = tst[-1]
        return solu

    # file extension extractor by page headers
    def FileExtenxion(self, link):
        r = requests.get(link)
        dicc = dict(r.headers)
        print('{} \n\n'.format(dicc))
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

    # to block page in host system
    def BlockListStatus(self, address_type):

        if address_type == 1:
            # inicial cofiguration
            default = ["127.0.0.1	localhost", "127.0.1.1	adrian-VirtualBox", "# The following lines are desirable for IPv6 capable hosts",
                       "::1     ip6-localhost ip6-loopback", "fe00::0 ip6-localnet", "ff00::0 ip6-mcastprefix", "ff02::1 ip6-allnodes", "ff02::2 ip6-allrouters"]

            # add blacklist
            blacklist = []
            for r in database.select_allip_blacklist():
                blacklist.append(r[0])

            # check if the list is not enty
            if len(blacklist) > 0:
                for nw in blacklist:
                    default.append("localhost " + nw)

            # write host file
            with open(host_path, 'w') as file:
                for df in default:
                    file.write(df+"\n")

        elif address_type == 3:

            # inicial cofiguration
            default = ["127.0.0.1	localhost", "127.0.1.1	adrian-VirtualBox", "# The following lines are desirable for IPv6 capable hosts",
                       "::1     ip6-localhost ip6-loopback", "fe00::0 ip6-localnet", "ff00::0 ip6-mcastprefix", "ff02::1 ip6-allnodes", "ff02::2 ip6-allrouters"]

            # add blacklist
            blacklist = []
            for r in database.select_all_blacklist():
                blacklist.append(r[0])

            # check if the list is not enty
            if len(blacklist) > 0:
                for nw in blacklist:
                    default.append("proyectoadrianitt.ddns.net " + nw)

            # write host file
            with open(host_path, 'w') as file:
                for df in default:
                    file.write(df+"\n")

    def handle_client(self, connection):
        # greeting header
        # read and unpack 2 bytes from a client

        version, nmethods = connection.recv(2)

        #-print("Version: {} , Nmethods: {}  \n\n\n".format(version,nmethods))

        # get available methods [0, 1, 2]
        methods = self.get_available_methods(nmethods, connection)

        #-print("methods: {}  \n".format(methods))

        # accept only USERNAME/PASSWORD auth
        if 2 not in set(methods):
            # close connection
            connection.close()
            return

        # send welcome message
        connection.sendall(bytes([SOCKS_VERSION, 2]))

        if not self.verify_credentials(connection):
            return

        # request (version=5)
        version, cmd, _, address_type = connection.recv(4)

        print("\nVersion: {} , CMD: {}, Addr_type: {}  \n".format(
            version, cmd, address_type))

        if address_type == 1:  # IPv4
            address = socket.inet_ntoa(connection.recv(4))
            p = address.decode('UTF-8')
            print('prueva de ip: {}'.format(p))

            if database.ipdomainblocked(p):

                print("*La direccion siguiente: {} no esta permitida \n\n".format(p))
                self.BlockListStatus(address_type)
                address = 'proyectoadrianitt.ddns.net'.encode('UTF-8')
                print(address)

            print("-{}".format(address))

        elif address_type == 3:  # Domain name
             
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)

            print("Este es lo que mide el dominio: {}".format(domain_length))
            p = address
            print('prueva de  nombre de  dominio: {}'.format(p))

            if database.domainblocked(p):
                 
                print("*La direccion siguiente: {} no esta permitida \n\n".format(p))
                address = 'proyectoadrianitt.ddns.net'.encode('UTF-8')

                print(address)

            address = socket.gethostbyname(address)

        # convert bytes to unsigned short array
        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        print("*Port number: {}\n".format(port))

        try:
            if cmd == 1:  # CONNECT
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
                print(bind_address)
                print("\n\n* Conectado a {} por el puerto {}".format(address, port))

            else:
                connection.close()

            addr = int.from_bytes(socket.inet_aton(
                bind_address[0]), 'big', signed=False)
            port = bind_address[1]

            reply = b''.join([
                SOCKS_VERSION.to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(1).to_bytes(1, 'big'),
                addr.to_bytes(4, 'big'),
                port.to_bytes(2, 'big')
            ])
        except Exception as e:
            # return connection refused error
            reply = self.generate_failed_reply(address_type, 5)

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("****** Reply:  {}".format(reply))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        connection.sendall(reply)

        # establish data exchange
        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(connection, remote)

        connection.close()

    def exchange_loop(self, client, remote):
        while True:
            # wait until client or remote is available for read
            r, w, e = select.select([client, remote], [], [])

            if client in r:
                data = client.recv(4096)
                if remote.send(data) <= 0:
                    break

            if remote in r:
                data = remote.recv(4096)
                if client.send(data) <= 0:
                    break

    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])

    def verify_credentials(self, connection):
        version = ord(connection.recv(1))  # should be 1

        username_len = ord(connection.recv(1))
        username = connection.recv(username_len).decode('utf-8')

        password_len = ord(connection.recv(1))
        password = connection.recv(password_len).decode('utf-8')

        if username == self.username and password == self.password:
            # success, status = 0
            response = bytes([version, 0])
            connection.sendall(response)
            return True

        # failure, status != 0
        response = bytes([version, 0xFF])
        connection.sendall(response)
        connection.close()
        return False

    def get_available_methods(self, nmethods, connection):
        methods = []
        for i in range(nmethods):
            methods.append(ord(connection.recv(1)))
        return methods

    def run(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen()

        #-print("* El  Socks5 proxy  {}:{}".format(host, port))

        while True:
            conn, addr = s.accept()
            #-print("* Nueva conexiòn desde {}".format(addr))
            # -print("--------------------------------------")
            # -print(conn)
            # -print("--------------------------------------")
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()


if __name__ == "__main__":
    try:
        proxy = Proxy()
        proxy.run("10.0.0.60", 3128)
    except KeyboardInterrupt as e:
        print("\n[*] Apagando...")
        sys.exit(1)
