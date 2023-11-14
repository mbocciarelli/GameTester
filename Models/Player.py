from Models.Ressource import Ressource

class Player:
    name: str
    current_storage: Ressource

    def __init__(self, name):
        self.name = name
        self.current_storage = Ressource(0, 0, 0, 0)

    def display_reserve(self) -> str:
        message = f'Mes ressources : \n Wheat = {self.current_storage.Wheat}\n Wood = {self.current_storage.Wood}\n Stone = {self.current_storage.Stone}\n Gold = {self.current_storage.Gold}'
        return message