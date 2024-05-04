from utils.game_logging import logger
from utils.config import SRC_PATH
import importlib
import os


class Loader:
    def __init__(self):
        self.module_loaded = []

    def set_events_manager(self, events_manager):
        self.events_manager = events_manager

    def import_single_file_module(self, name):
        module = importlib.import_module(name)
        if hasattr(module, "subscriptions"):
            logger.debug(f"Found subscriptions in {name}")
            self.events_manager.multi_subscribe(module.subscriptions)
        if hasattr(module, "registrations"):
            logger.debug(f"Found registrations in {name}")
            self.events_manager.register(module.registrations)

    def import_multi_file_module(self, name):
        dir_name = name.replace(".", "/")
        if os.path.isfile(f"{SRC_PATH}/{dir_name}/render.py"):
            logger.debug(f"Found render.py in {name}")
            self.import_single_file_module(f"{name}.render")
        if os.path.isfile(f"{SRC_PATH}/{dir_name}/logic.py"):
            logger.debug(f"Found logic.py in {name}")
            self.import_single_file_module(f"{name}.logic")
        if os.path.isfile(f"{SRC_PATH}/{dir_name}/events.py"):
            logger.debug(f"Found events.py in {name}")
            self.import_single_file_module(f"{name}.events")

    def import_module(self, name):
        logger.debug(f"Processing module: {name}")
        dir_name = name.replace(".", "/")
        if os.path.isfile(f"{SRC_PATH}/{dir_name}.py"):
            # is a single-file module
            logger.debug(f"Is a single-file module: {name}")
            self.import_single_file_module(name)
        elif os.path.isdir(f"{SRC_PATH}/{dir_name}"):
            # is a multi-file module
            logger.debug(f"Is a multi-file module: {name}")
            self.import_multi_file_module(name)
        else:
            logger.error(f"Module not found: {name}")

    def import_modules(self, names):
        for name in names:
            self.import_module(name)
