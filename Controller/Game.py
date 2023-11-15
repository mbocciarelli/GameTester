from os import system, name
import logging
from typing import List

from Models.Player import Player
from Models.Batiment import Base

from Controller.Loader.Loader import load_json, load_upgrade_to

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
        self.player : Player = Player(player_name)
        self.base : Base = None
        self.global_time: int = 0

    def game_loop(self) -> None:

        self.base = load_json()
        if name == 'nt': 
            clear = lambda: system('cls')
        else: 
            clear = lambda: system('clear')

        args = ""

        clear()
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

            if self.Is_necessary_to_upgrade_Chateau(self.global_time) == True:
                self.Upgrade_Chateau()

            clear()

            self.display_timing(time)
            self.to_string()
            pass

        logger.info("Stop loop Game")


    def Is_necessary_to_upgrade_Chateau(self, time) -> bool:
        match self.base.chateau.lvl:
            case 1:
                if time >= (15 * 60): # 15 mins
                    return True
            case 2:
                if time >= (30 * 60): # 30 mins
                    return True
            case 3:
                if time >= (1 * 60 * 60): # 1 h
                    return True
            case 4:
                if time >= (1 * 60 * 60 + 45 * 60): # 1 h 45 mins
                    return True
            case _:
                return False
        return False

    def Upgrade_Chateau(self):
        self.base.chateau.lvl += 1
        cost, _ = load_upgrade_to("chateau", self.base.chateau.lvl)
        self.base.chateau.cost = cost
        return

    def display_timing(self, time: int) -> None:
        logger.debug("Timing : %s", time)
        hour = self.global_time // 3600
        min = (self.global_time % 3600) // 60
        sec = ((self.global_time % 3600) % 60)

        logger.info("Timing Global : %sh %sm %ss", hour, min, sec)

    def to_string(self) -> None:
        logger.info(f'')
        logger.info(f'Chateau - ' + self.base.chateau.name + f'({self.base.chateau.lvl})')
        logger.info(f'')
        logger.info(f'Base - ' + self.base.display_reserve() + '\n')
        logger.info(f'Player - ' + self.player.display_reserve())
        logger.info(f'')
        logger.info(f'Batiments - ' + self.base.display_infos())
        logger.info(f'')