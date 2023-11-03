import logging

from Models.Player import Player
from Models.Batiment import Batiment, Collecteur, Storage, Base

logger = logging.getLogger(__name__)

def timing_to_add(timing: str) -> int:
    time_in_seconds = 0

    if timing.endswith("s"):
        time_in_seconds = int(timing.removesuffix("s"))
    elif timing.endswith("m"):
        time_in_seconds = int(timing.removesuffix("m")) * 60
    elif timing.endswith("h"):
        time_in_seconds = int(timing.removesuffix("h")) *60 *60

    return time_in_seconds

class Game:
    def __init__(self, player_name: str) -> None:
        self.player = Player(player_name)
        
        self.base = Base()

    def game_loop(self) -> None:

        args = ""

        while args!="s":
            args = input("input : ")
            time = timing_to_add(args)
            logger.debug("Timing : %s", time)
            pass

        logger.info("Stop loop Game")

    