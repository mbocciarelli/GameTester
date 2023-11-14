import os
import logging
import json
from typing import List

from Models.Player import Player
from Models.Batiment import Base, Collecteur, Ressource, Storage

logging.basicConfig(
    level=logging.DEBUG,
    format=""
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def timing_to_add(timing: str) -> int:
    time_in_seconds = 0

    if timing.endswith("s"):
        time_in_seconds = int(timing.removesuffix("s"))
    elif timing.endswith("m"):
        time_in_seconds = int(timing.removesuffix("m")) * 60
    elif timing.endswith("h"):
        time_in_seconds = int(timing.removesuffix("h")) * 3600

    return time_in_seconds

class Game:
    def __init__(self, player_name: str) -> None:
        self.player = Player(player_name)
        self.base = Base()
        self.global_time: int = 0

    def game_loop(self) -> None:

        self.load_json()
        clear = lambda: os.system('cls')

        args = ""

        while args!="q":
            args = input("input : ")
            time = timing_to_add(args)
            self.global_time += time

            for c in self.base.collecteurs:
                c.timing += time
                if c.timing >= c.timing_max:
                    add_ressource = c.timing // c.timing_max
                    self.player.current_storage += c.ressource * add_ressource

                    c.timing = c.timing % c.timing_max

            clear()

            self.display_timing(time)
            self.to_string()
            pass

        logger.info("Stop loop Game")

    def display_timing(self, time: int) -> None:
        logger.debug("Timing : %s", time)
        hour = self.global_time // 3600
        min = (self.global_time % 3600) // 60
        sec = ((self.global_time % 3600) % 60)

        logger.info("Timing Global : %sh %sm %ss", hour, min, sec)

    def to_string(self) -> None:
        logger.info(f'')
        logger.info(f'Base - ' + self.base.display_reserve() + '\n')
        logger.info(f'Player - ' + self.player.display_reserve())
        logger.info(f'')
        logger.info(f'Batiments - ' + self.base.display_infos())
        logger.info(f'')

    def load_json(self) -> None:
        f = open('Data/Batiment.json', "r")
        data = json.loads(f.read())

        chateau = data['chateau']
        cost = Ressource(chateau["lvls"]["1"]['cost']['wheat'], chateau["lvls"]["1"]['cost']['wood'], chateau["lvls"]["1"]['cost']['stone'], chateau["lvls"]["1"]['cost']['gold'])
        ressource = Ressource(chateau["lvls"]["1"]['ressource']['wheat'], chateau["lvls"]["1"]['ressource']['wood'], chateau["lvls"]["1"]['ressource']['stone'], chateau["lvls"]["1"]['ressource']['gold'])
        self.base.chateau = Storage(chateau['name'], chateau['lvl'], cost, ressource)

        for collecteur in data['collecteurs']:
            cost = Ressource(collecteur["lvls"]["1"]['cost']['wheat'], collecteur["lvls"]["1"]['cost']['wood'], collecteur["lvls"]["1"]['cost']['stone'], collecteur["lvls"]["1"]['cost']['gold'])
            ressource = Ressource(collecteur["lvls"]["1"]['ressource']['wheat'], collecteur["lvls"]["1"]['ressource']['wood'], collecteur["lvls"]["1"]['ressource']['stone'], collecteur["lvls"]["1"]['ressource']['gold'])

            self.base.collecteurs.append(Collecteur(
                collecteur['name'],
                collecteur['lvl'],
                cost,
                ressource,
                collecteur['timing_max']
            ))

        f.close()