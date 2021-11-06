from sys import stdout
from loguru import logger

from configs import AppConfig

logger.remove()
logger.add(stdout, level=AppConfig.LOG_LEVEL, colorize=AppConfig.LOG_COLORIZE)

Logger = logger
