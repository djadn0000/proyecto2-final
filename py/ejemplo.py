import socket
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/etc/ssl/certs/ssl-cert-snakeoil.pem', '/etc/ssl/private/ssl-cert-snakeoil.key')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('127.0.0.1', 3128 ))
sock.listen(5)
ssock= context.wrap_socket(sock, server_side=True) 
conn, addr = ssock.accept()