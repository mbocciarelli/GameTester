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
    type: str
    ressource: Ressource

    def __init__(self, name, type, lvl, cost, ressource, timing_max):
        super().__init__(name, lvl, cost)
        self.ressource = ressource
        self.timing_max = timing_max
        self.timing = 0
        self.type = type
    
    def display_info(self) -> str:
        message = f'{self.name}({self.lvl})'
        return message
    
    def Upgrade(self):
        self.lvl += 1
        cost, ressource = load_upgrade_to("collecteurs", self.type, self.lvl)
        self.cost = cost
        self.ressource = ressource
        return

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
        # self.chateau = Storage("Chateau", 1, Ressource(0, 0, 0, 0), Ressource(5000, 5000, 5000, 5000))
        return

    def get_max_reserve(self) -> Ressource:
        if self.reserve is not None:
            return self.chateau.storage + self.reserve.storage
        return self.chateau.storage
    
    def display_reserve(self) -> str:
        ressource = self.get_max_reserve()
        message = f'Ressource Max : \n Wheat = {ressource.Wheat}\n Wood = {ressource.Wood}\n Stone = {ressource.Stone}\n Gold = {ressource.Gold}'
        return message
    
    def log_display_reserve(self) -> str:
        ressource = self.get_max_reserve()
        message = f'({ressource.Wheat}, {ressource.Wood}, {ressource.Stone}, {ressource.Gold})'
        return message
    
    def display_infos(self) -> str:
        message = ''
        for c in self.collecteurs:
            message += c.display_info()
            if self.collecteurs.index(c) != (len(self.collecteurs) - 1):
                message += ', '
        
        return message
    
    def Upgrade_Chateau(self):
        self.chateau.lvl += 1
        cost, storage = load_upgrade_to("chateau", "", self.chateau.lvl)
        self.chateau.cost = cost
        self.chateau.storage = storage
        return
    

from Controller.Loader.Loader import load_upgrade_to