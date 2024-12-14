import time
from ..event_pkg import Event

ZZZ_TIME: float = 0.05

class Client:
    def __init__(self, name: str = "none"):
        self.e_call: Event = Event(f"{name} client call")
        self.response = None

    def call_sync(self, *args):
        self.e_call.trigger(*args)
        while self.response == None:
            time.sleep(ZZZ_TIME)
        return self.response
    