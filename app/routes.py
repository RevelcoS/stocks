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
    stocks_table = stock.int_table_data(stock.read_table())
    graph_table = stock.read_table()
    return render_template(
        "stocks.html",
        stocks_table=stocks_table["stocks"],
        graph_table=graph_table["stocks"],
        rounds=list(range(graph_table["next_round"])),
        colors_table={"Tech":"#2d55d9", "Bio":"#31E987", "Calc":"#f2a314", "CPy":"#e60000"},
        leading_stock=stock.leading_stock())