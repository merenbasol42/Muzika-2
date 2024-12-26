from typing import Any

class IConfigInterface:
    def import_json(self, config_dict: dict[str, Any]):
        for key, value in config_dict.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def export_json(self) -> dict[str, Any]: 
        return {
            key : value 
            for key, value in vars(self).items() 
                if not key.startswith("_")
        }

class ConfigInterface(IConfigInterface):
    def __init__(self):
        self.theme = None 
        self.language = None 
        self.lang_dir = None
        self.assets_dir = None 
        self.icons_dir = None
        self.sounds_dir = None
        self.pls_dir = None

import json

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

