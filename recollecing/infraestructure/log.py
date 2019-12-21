import logging
import logging.config


def setup_log():
    """Defines the logging."""
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                }
            },
            "root": {"level": "INFO", "handlers": ["console"]},
        }
    )
    logging.captureWarnings(True)  # Log warnings instead of printing them
