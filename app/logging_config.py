
import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s (%(filename)s:%(lineno)d) - %(message)s"
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
            "level": "DEBUG",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "geonews.log",
            "formatter": "detailed",
            "level": "DEBUG",
        },
    },

    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}
