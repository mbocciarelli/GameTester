from datetime import datetime
from typing import Any, Dict, List, Optional
from Models.Ressource import Ressource

class Batiment:
    name: str
    lvl: int
    cost: Ressource

class Collecteur(Batiment):
    timing: int
    ressource: Ressource

class Storage(Batiment):
    storage: Ressource