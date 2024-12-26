from mizika import Mizika as _Mizika
from commpy.event_pkg import Event
from commpy.service_pkg import Service

class Mizika(_Mizika):
    def __init__(self, pls_dir: str):
        super().__init__(pls_dir)

        #
        # Events
        #

        #
        # Services
        #