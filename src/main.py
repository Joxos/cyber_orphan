from utils.config import PLUGINS_PATH
from utils.utils import get_whole_runtime
from core.events import DEFAULT_EVENT_LIST
import arcade

if __name__ == "__main__":
    runtime, plugin_manager, events_manager, game = get_whole_runtime()
    events_manager.register(DEFAULT_EVENT_LIST)
    plugin_manager.load_plugins(PLUGINS_PATH)
    plugin_manager.setup_plugins()
    game.setup()
    arcade.run()
