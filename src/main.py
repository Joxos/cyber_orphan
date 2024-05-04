from core.runtime import Runtime
from utils.config import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_TITLE
import arcade

if __name__ == "__main__":
    runtime = Runtime(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE)
    arcade.run()
