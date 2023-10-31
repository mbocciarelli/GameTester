import logging
import _thread

from Models.Player import Player

logger = logging.getLogger(__name__)

args = None

def game_input(threadname):
        global args
        args = input("input : ")

class Game:
    def __init__(self, player_name: str) -> None:
        self.player = Player(player_name)

    def game_loop(self):
        try:
            _thread.start_new_thread(game_input, ("UI",) )
            while args==None:
                logger.info("Coucou")
                pass
            logger.info("Stop loop Game")
        except:
            logger.debug("Error: unable to start thread")
            

    