from flask import render_template, url_for
from app import app
from app import ConfigHandler, TableHandler
from app import algorithm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/stocks")
def stocks():
    algorithm.refresh_prices()
    config_data = ConfigHandler.read_data()
    graph_table = TableHandler.read_data()
    stocks_table = algorithm.int_table_data(graph_table)
    return render_template(
        "stocks.html",
        stocks_table=stocks_table["stocks"],
        graph_table=graph_table["stocks"],
        table_rounds=list(range(stocks_table["next_round"])),
        graph_rounds=list(range(config_data["max_rounds"])),
        colors_table=config_data["companies"],
        leading_stock=algorithm.leading_stock())