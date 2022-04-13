from msilib.schema import tables
from flask import render_template, url_for
from app import app
from app import ConfigHandler, TableHandler
from app.stocks import stock

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/stocks")
def stocks():
    stock.refresh_prices()
    config_data = ConfigHandler.read_data()
    TableHandler.update_data()
    graph_table = TableHandler.read_data()
    stocks_table = stock.int_table_data(graph_table)
    return render_template(
        "stocks.html",
        stocks_table=stocks_table["stocks"],
        graph_table=graph_table["stocks"],
        rounds=list(range(graph_table["next_round"])),
        colors_table=config_data["companies"],
        leading_stock=stock.leading_stock())