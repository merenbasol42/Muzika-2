from .utils import *
from ..msg_if import MsgI

class Event:
    def __init__(self, name: str):
        self.name: str = name
        self.subs: list = []
    
    def subscribe(self, cb):
        count: int = self.subs.count(cb)
        if count != 0: raise AlreadySubscribedError  

        self.subs.append(cb)

    def trigger(self, *args):
        for sub in self.subs: 
            sub(*args)

class EventWType(Event):
    def __init__(self, name, msg_type: MsgI):
        super().__init__(name)