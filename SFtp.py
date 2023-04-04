import os, socket
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
os.system("clear")

FTP_PORT = 3690
FTP_DIRECTORY = os.getcwd()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("45.171.66.114", 80))
IP = s.getsockname()[0]
s.close()

print("")
print(f'DIRECCION: ftp://{IP}:{FTP_PORT}')
print("")
print(f'DIRECTORIO RAIZ: {FTP_DIRECTORY}')
print("")


authorizer = DummyAuthorizer()
authorizer.add_anonymous(FTP_DIRECTORY, perm='elradfmw')

handler = FTPHandler
handler.authorizer = authorizer
handler.banner = 'T3nshi Servidor Ftp'
handler.passive_ports = range(50000, 55535)

address = ('', FTP_PORT)
server = FTPServer(address, handler)

server.max_cons = 256
server.max_cons_per_ip = 5

server.serve_forever()
