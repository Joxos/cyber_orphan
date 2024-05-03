from core.events import EventsManager, DEFAULT_EVENT_LIST, BeforeGameInit
from core.game import Game
from utils.config import DEFAULT_MODULES, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_TITLE
import arcade

if __name__ == "__main__":
    events_manager = EventsManager()
    events_manager.register(DEFAULT_EVENT_LIST)
    events_manager.import_modules(DEFAULT_MODULES)
    events_manager.verbose_subscription_info()
    events_manager.new_event(BeforeGameInit())

    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, events_manager)
    game.setup()
    arcade.run()
