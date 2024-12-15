import time
from ..utils import UnmatchingMsgType
from ..event_pkg import Event
from .srv_if import SrvMsgI
from typing import Type

ZZZ_TIME: float = 0.05

class Client:
    def __init__(self, name: str = "none"):
        self.e_call: Event = Event(f"{name} client call")
        self.response = None

    def call_sync(self, *args):
        self.response = None
        self.e_call.trigger(*args)
        while self.response == None:
            time.sleep(ZZZ_TIME)
        return self.response

class ClientWType(Client):
    def __init__(self, srv_type: Type[SrvMsgI], name = "none"):
        self.type: SrvMsgI = srv_type
        super().__init__(name)

    def call_sync(self, msg: SrvMsgI) -> SrvMsgI:
        if not isinstance(msg, self.type): 
            raise UnmatchingMsgType()
        return super().call_sync(msg)
