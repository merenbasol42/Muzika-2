from ...msg_if import MsgI
from typing import Generic, TypeVar

T = TypeVar('T')

class MTSimple(MsgI, Generic[T]):  # MTList generic bir sınıf
    def __init__(self):
        self.data: T 
        super().__init__()  