from Models.Ressource import Ressource

class Player:
    name: str
    current_storage: Ressource
    storage_max: Ressource

    def __init__(self, name):
        self.name = name