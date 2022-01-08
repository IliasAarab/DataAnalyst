"""Simple logger class to flexibly log src code
"""

## Main libs
# ---------------
from datetime import datetime
from loguru import logger
import json
import sys
import os


class LoggerConfiguration:
    """flexible logger based on loguru.

    To disable the created logger at module level (e.g. when going into production) set:

    from .utils.logger import logger
    logger.disable(__name__)"""

    # Main format
    _format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> | <cyan>line {line}</cyan> | <level>{message}</level>",
    )
    # Resolve path
    this_dir, _ = os.path.split(__file__)

    def __init__(self) -> None:
        """Log level & handler are read from logging.json config file.
        In case you want to overwrite the configs, use the set_logger args."""
        self.log_level = self.get_config("logging.json", "LOG_LEVEL")
        self.handler = self.get_config("logging.json", "HANDLER")

    def get_config(self, config_key: str, config_file: str = "logging.json") -> str:
        """Get configuration settings from config file.

        Parameters
        ----------
        config_key : str
            configuration key from config value, config[key]= value
        config_file : str, optional
            configuration file to draw keys from, by default 'logging.json'

        Returns
        -------
        str
            Value associated with configuration key.
        """

        file = os.path.join(LoggerConfiguration.this_dir, f"configs/{config_file}")
        with open(file, encoding="utf-8") as f:
            config = json.load(f)
        return config[config_key]

    def set_logger(self, log_level: str = None, handler: str = None) -> None:
        """Creates a logger and adds formatted handlers to it.

        Parameters
        ----------
        log_level : str, optional
            standard loglevels, by default None.
            If None, then keeps log_level drawn from config file
        handler : str, optional
            'FILE' creates file handler
            'STREAM' creates stream handler
            'Both' creates both handlers, by default None
            If None, then keeps handler drawn from config file
        """
        if log_level is not None:
            self.log_level = log_level
        if handler is not None:
            self.handler = handler
        # Create new loggers
        logger.remove()
        if self.handler.lower() == "both":
            self.handler = "FILE/STREAM"
        if "stream" in self.handler.lower():
            # streaming handler
            logger.add(
                sys.stderr,
                format=LoggerConfiguration._format[0],
                level=self.log_level,
                colorize=True,
                backtrace=False,
            )
        if "file" in self.handler.lower():
            # file handler
            # now = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
            # file_name = f"log_book/logs_{now}.log"
            file_name = "log_book/logs.log"
            logger.add(
                os.path.join(LoggerConfiguration.this_dir, file_name),
                format=LoggerConfiguration._format[0],
                level=self.log_level,
                colorize=False,
                backtrace=False,
                retention="1 day",
            )
        self.logger = logger


# Create logger
log_config = LoggerConfiguration()
log_config.set_logger()
logger = log_config.logger
