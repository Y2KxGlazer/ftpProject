import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class UD_Server():
    _handler = None
    _authorizer = None

    def __init__(self):
        UD_Server._authorizer = DummyAuthorizer()

    def add_user(self, name, password):
        UD_Server._authorizer.add_user(name, password, '.', perm='elradfmwMT')

    def ftp_start(self):
        UD_Server._handler = FTPHandler
        UD_Server._handler.authorizer = UD_Server._authorizer

        UD_Server._handler.banner = "pyftpdlib based ftpd ready."
        address = ('', 2121)
        server = FTPServer(address,  UD_Server._handler)
        server.max_cons = 256
        server.max_cons_per_ip = 5
        server.serve_forever()
