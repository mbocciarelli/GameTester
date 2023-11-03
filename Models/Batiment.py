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
    ressource: Ressource

    def __init__(self, name, lvl, cost, ressource, timing):
        super(Collecteur, self).__init__(name, lvl, cost)
        self.ressource = ressource
        self.timing = timing

class Storage(Batiment):
    storage: Ressource

    def __init__(self, name, lvl, cost, storage):
        super(Collecteur, self).__init__(name, lvl, cost)
        self.storage = storage

class Base:
    chateau: Storage = None
    reserve: Storage = None
    collecteurs: List[Collecteur] = []

    def __init__(self):
        self.chateau = Storage("Chateau", 1, Ressource(0, 0, 0, 0), Ressource(5000, 5000, 5000, 5000))

    def get_max_reserve(self) -> Ressource:
        if self.reserve is not None:
            return self.chateau.storage + self.reserve.storage
        return self.chateau.storage