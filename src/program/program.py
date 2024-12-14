from ..mizika import Mizika 

class Program:
    def __init__(self, pls_dir_path: str):
        self.mizika: Mizika = Mizika(pls_dir_path)
    
    def run(self):
        print("hi")
        while True:
            pass


class IManagerI:
    pass

class ManagerIFEtoBE(IManagerI):
    pass

class ManagerIBEtoFE(IManagerI):
    pass