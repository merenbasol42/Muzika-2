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