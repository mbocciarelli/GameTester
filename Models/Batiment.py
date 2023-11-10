from datetime import datetime
from typing import Any, Dict, List, Optional
from Models.Ressource import Ressource

class Batiment:
    name: str
    lvl: int
    cost: Ressource

    def __init__(self, name, lvl, cost):
        self.name = name
        self.lvl = lvl
        self.cost = cost

class Collecteur(Batiment):
    timing: int
    timing_max: int
    ressource: Ressource

    def __init__(self, name, lvl, cost, ressource, timing_max):
        super().__init__(name, lvl, cost)
        self.ressource = ressource
        self.timing_max = timing_max
        self.timing = 0

class Storage(Batiment):
    storage: Ressource

    def __init__(self, name, lvl, cost, storage):
        super().__init__(name, lvl, cost)
        self.storage = storage

class Base:
    chateau: Storage
    reserve: Optional[Storage] = None
    collecteurs: List[Collecteur] = []

    def __init__(self):
        self.chateau = Storage("Chateau", 1, Ressource(0, 0, 0, 0), Ressource(5000, 5000, 5000, 5000))

    def get_max_reserve(self) -> Ressource:
        if self.reserve is not None:
            return self.chateau.storage + self.reserve.storage
        return self.chateau.storage
    
    def to_string(self) -> str:
        ressource = self.get_max_reserve()
        message = f'Ressource Max : \n Wheat = {ressource.Wheat}, Wood = {ressource.Wood}, Stone = {ressource.Stone}, Gold = {ressource.Gold}'
        return message