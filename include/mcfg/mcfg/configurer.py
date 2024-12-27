import json

from .cfg_interface import ConfigInterface

class Configurer:
    '''Singleton class to manage configuration'''
    __instance = None
    def __new__(cls, *args, **kwargs):
        if Configurer.__instance is not None: return Configurer.__instance
        return super().__new__(cls)

    def __init__(self, path: str = None):
        if Configurer.__instance is not None: return
        if path is None: raise ValueError("path cannot be None")
        Configurer.__instance = self
        self.path = path
        self.cfg: ConfigInterface = ConfigInterface()
        self.load()

    def load(self):
        '''Load configuration from file'''
        try:
            with open(self.path, 'r') as f:
                self.cfg.import_json(
                    json.load(f)
                )
        except Exception:
            self.save()
            self.load()            

    def save(self):
        '''Save configuration to file'''
        with open(self.path, 'w') as f:
            json.dump(
                self.cfg.export_json(),
                f,
                indent = 4
            )

