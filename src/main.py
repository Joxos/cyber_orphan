from utils.config import PLUGINS_PATH
from utils.utils import get_whole_runtime
import arcade

if __name__ == "__main__":
    runtime, plugin_manager, events_manager, game = get_whole_runtime()
    plugin_manager.load_plugins(PLUGINS_PATH)
    game.setup()
    arcade.run()
