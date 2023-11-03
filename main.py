import logging
import json

from Controller.Game import Game

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Hey !")

    player_name = input("Player name : ")

    game = Game(player_name)
    game.game_loop()
    return


if __name__ == "__main__":
    main()