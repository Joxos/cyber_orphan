from loguru import logger
import sys
from utils.config import LOG_LEVEL

logger.remove()
logger.add(sys.stderr, level=LOG_LEVEL, colorize=True)
