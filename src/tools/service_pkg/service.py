from .server import Server
from .client import Client
from .utils import *

class Service:
    def __init__(self, name: str):
        self.name = name
        self.server: Server = None
        self.clients: list[Client] = []

    def __cb(self, index: int, *args):
        response = self.server.cb(*args)
        self.clients[index].response = response

    def add_client(self, client: Client):
        def cb(*args):
            self.__cb(len(self.clients), *args)
        client.e_call.subscribe(cb)

    def add_service(self, server: Server):
        if server != None: raise AlreadyHasAServer(
            "This service already has a server"
        )
        self.server = server