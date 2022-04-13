from flask import Flask
from app.stocks.file_handler import JsonHandler

app = Flask(__name__)
ConfigHandler = JsonHandler("config.json", read_only=True)
LogHandler = JsonHandler("log.json")
TableHandler = JsonHandler("table.json")

from app import routes