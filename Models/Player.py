from Models.Ressource import Ressource

class Player:
    name: str
    current_storage: Ressource

    def __init__(self, name):
        self.name = name
        self.current_storage = Ressource(0, 0, 0, 0)

    def to_string(self) -> str:
        message = f'Mes ressources : \n Wheat = {self.current_storage.Wheat}, Wood = {self.current_storage.Wood}, Stone = {self.current_storage.Stone}, Gold = {self.current_storage.Gold}'
        return message