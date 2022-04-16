from flask import Flask, url_for
from flask import logging as flog
from app.file_handler import JsonHandler
from logging.handlers import RotatingFileHandler
import logging, os

app = Flask(__name__)

# Json
ConfigHandler = JsonHandler("config.json", read_only=True)
ActionsHandler = JsonHandler("actions.json")
TableHandler = JsonHandler("table.json")

# Logging
if not os.path.exists("logs"):
    os.mkdir("logs")

formatter = logging.Formatter(fmt="[%(asctime)s %(levelname)s]: %(message)s", datefmt="%H:%M:%S")

log_handler = RotatingFileHandler("logs/stocks.log", maxBytes=5000, backupCount=10)
log_handler.setFormatter(formatter)
log_handler.setLevel(logging.INFO)
app.logger.addHandler(log_handler)

flog.default_handler.setFormatter(formatter)
app.logger.setLevel(logging.INFO)
app.logger.info("Starting Stocks App")

from app import routes