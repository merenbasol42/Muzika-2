from ..utils import AlreadyHasAServer, UnmatchingMsgType
from .client import Client, ClientWType
from .server import Server, ServerWType
from .srv_if import SrvMsgI

class Service:
    def __init__(self, name: str):
        self.name = name
        self.server: Server = None
        self.clients: list[Client] = []

    def __cb(self, index: int, *args):
        response = self.server.cb(*args)
        self.clients[index].response = response

    def add_client(self, client: Client):
        index = len(self.clients)
        def cb(*args): self.__cb(index, *args)       
        client.e_call.subscribe(cb)
        self.clients.append(client)

    def add_service(self, server: Server):
        if self.server != None: raise AlreadyHasAServer(
            "This service already has a server"
        )
        self.server = server

class ServiceWType(Service):
    def __init__(self, type: type[SrvMsgI], name: str = "none"):
        self.type = type
        super().__init__(name)

    def add_client(self, client: ClientWType):
        if client.type != self.type:
            raise UnmatchingMsgType(
                expected = self.type,
                received = client.type
            )
        return super().add_client(client)

    def add_service(self, server: ServerWType):
        if server.type != self.type:
            raise UnmatchingMsgType(
                expected = self.type,
                received = server.type
            )
        return super().add_service(server)