from utils.utils import get_whole_runtime
import arcade

if __name__ == "__main__":
    runtime, plugin_manager, events_manager, game = get_whole_runtime()
    arcade.run()
