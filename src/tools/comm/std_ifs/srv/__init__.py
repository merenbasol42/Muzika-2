from ..msg.simple import MTSimple
from ...service_pkg.srv_if import SrvMsgI
from ..msg import ListInt, Int

class Add(SrvMsgI):
    def __init__(self):
        self.request: ListInt = ListInt()
        self.response: Int = Int()
        super().__init__()
