from core.events import EventsManager, DEFAULT_EVENT_LIST, BeforeGameInit
from core.loader import Loader
from core.game import Game
from utils.config import DEFAULT_MODULES


class Runtime:
    def __init__(self, width, height, title):
        self.loader = Loader()

        self.events_manager = EventsManager()
        self.loader.set_events_manager(self.events_manager)
        self.events_manager.register(DEFAULT_EVENT_LIST)

        self.events_manager.new_event(BeforeGameInit())
        self.game = Game(width, height, title)
        self.events_manager.set_game(self.game)

        self.loader.import_modules(DEFAULT_MODULES)
        self.events_manager.verbose_subscription_info()
        self.game.setup(self.events_manager)
