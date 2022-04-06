from flask import render_template, url_for
from app import app
from app.stocks import stock

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/stocks")
def stocks():
    stock.refresh_prices()
    table = stock.read_table()
    return render_template(
        "stocks.html",
        stocks_table=table["stocks"],
        rounds=range(table["next_round"]))