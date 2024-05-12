class Runtime:
    def __init__(self):
        self.events_manager = None
        self.game = None
        self.plugin_manager = None
        # self.events_manager = EventsManager()
        # self.events_manager.register(DEFAULT_EVENT_LIST)
        # self.events_manager.verbose_subscription_info()

        # self.events_manager.new_event(BeforeGameInit())
        # self.game = Game(width, height, title)
        # self.events_manager.new_event(OnGameInit())

        # self.game.setup(self.events_manager)
        # self.events_manager.new_event(OnGameSetup())
