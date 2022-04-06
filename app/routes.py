from flask import render_template
from app import app
from app.stocks import stock

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/stocks")
def stocks():
    stock.refresh_prices()
    return stock.read_table()