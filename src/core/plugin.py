from core.runtime import Runtime
from utils.game_logging import logger
import os
import importlib.util
import concurrent.futures
import inspect


class PluginConfig:
    def __init__(self):
        pass


class Plugin:
    def __init__(self, runtime: Runtime):
        self.runtime = runtime

    def setup(self):
        self.runtime.events_manager.register(self.registrations)
        self.runtime.events_manager.multi_subscribe(self.subscriptions)

    @property
    def registrations(self):
        """Return a list of event classes."""
        return []

    @property
    def subscriptions(self):
        """Return a dictionary of event classes and their callbacks."""
        return {}


class PluginManager:
    def __init__(self):
        self.plugins = []
        self.runtime = None

    def load_plugins(self, plugin_dir):
        plugin_dir = os.path.abspath(plugin_dir)

        py_files = [name for name in os.listdir(plugin_dir) if name.endswith(".py")]
        filepaths = [os.path.join(plugin_dir, name) for name in py_files]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_file = {
                executor.submit(self.load_plugin, filepath): filepath
                for filepath in filepaths
            }
            for future in concurrent.futures.as_completed(future_to_file):
                self.plugins.extend(future.result())

        logger.info("Plugins loaded:")
        for plugin in self.plugins:
            logger.info(f"  - {plugin.__class__.__name__}")

    def load_plugin(self, filepath):
        module_name = os.path.basename(filepath).rstrip(".py")
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        # check all the classes
        local_plugins = [
            obj(self.runtime)
            for name, obj in inspect.getmembers(mod)
            if inspect.isclass(obj) and issubclass(obj, Plugin) and obj is not Plugin
        ]
        return local_plugins

    def activate_plugins(self):
        for plugin in self.plugins:
            plugin.activate(self.runtime)


if __name__ == "__main__":
    manager = PluginManager()
    manager.load_plugins("core.plugins")
    print(manager.plugins)
