from os import system, name
import logging
from typing import List, Dict

from Models.Player import Player
from Models.Batiment import Base

from Controller.Loader.Loader import load_json, load_upgrade_to, write_in_log_file

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

        self.log_init()
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
                self.base.Upgrade_Chateau()

            # if self.Is_necessary_to_add_collecteur() == True:
            #     self.Add_Collecteur()

            clear()

            self.display_timing(time)
            self.to_string()
            self.log_display(args)
            pass

        logger.info("Stop loop Game")


    def Is_necessary_to_upgrade_Chateau(self, time) -> bool:
        if (self.player.current_storage >= self.base.chateau.cost) == False: 
            return False

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
    
    def calculate_time(self, time: int) -> Dict:
        result = {}
        result["hour"] = self.global_time // 3600
        result["min"] = (self.global_time % 3600) // 60
        result["sec"] = ((self.global_time % 3600) % 60)
        return result

    def display_timing(self, time: int) -> None:
        logger.debug("Timing : %s", time)
        timing = self.calculate_time(time)

        logger.info("Timing Global : %sh %sm %ss", timing["hour"], timing["min"], timing["sec"])

    def to_string(self) -> None:
        logger.info(f'')
        logger.info(f'Chateau - ' + self.base.chateau.name + f'({self.base.chateau.lvl})')
        logger.info(f'')
        logger.info(f'Base - ' + self.base.display_reserve() + '\n')
        logger.info(f'Player - ' + self.player.display_reserve())
        logger.info(f'')
        logger.info(f'Batiments - ' + self.base.display_infos())
        logger.info(f'')

    def log_init(self) -> None:
        message = "\nNew Partie\n"
        write_in_log_file(message)

    def log_display(self, args) -> None:
        message = args
        message += ' - '
        message += self.base.chateau.name + f'({self.base.chateau.lvl})'
        message += ' - '
        message += self.base.log_display_reserve()
        message += ' - '
        message += self.player.log_display_reserve()
        message += ' - '
        message += self.base.display_infos()
        message += '\n'

        write_in_log_file(message)