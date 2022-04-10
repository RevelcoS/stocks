import json

def read_local_json(name):
    with open(f"app/stocks/{name}", "r") as _file:
        data = json.load(_file)
    return data

def write_local_json(name, data):
    with open(f"app/stocks/{name}", "w") as _file:
        data = json.dump(data, _file, indent=4)



def calculate_prices(stock):
    '''
    Calculates a list of prices for each round
    (strating with 0 round) for a particular stock
    '''
    config_data = read_local_json("config.json")
    companies_data = config_data["companies"]
    algorithm_data = config_data["algorithm"]
    delta_data = algorithm_data["delta_prices"]
    log_data = read_local_json("log.json")

    prices = [algorithm_data["start_price"]]
    for _round in range(1, len(log_data)+1):
        delta = 0
        for action in log_data[str(_round)]:
            passed, station, = action.split()
            if station in companies_data[stock]["stations"]:
                if passed == "+":
                    delta += delta_data["+"]
                elif passed == "0":
                    delta += delta_data["0"]
                elif passed == "-":
                    delta += delta_data["-"]
        prices.append(prices[-1] + delta)

    return prices


def str_round_table_data(table_data):
    config_data = read_local_json("config.json")
    float_precision = config_data["algorithm"]["float_precision"]
    stocks_table = table_data["stocks"]
    for stock in stocks_table:
        for _round in range(len(stocks_table[stock])):
            stocks_table[stock][_round] = format(float(stocks_table[stock][_round]), f".{float_precision}f")
    return table_data

def int_table_data(table_data):
    stocks_table = table_data["stocks"]
    for stock in stocks_table:
        for _round in range(len(stocks_table[stock])):
            stocks_table[stock][_round] = round(float(stocks_table[stock][_round]))
    return table_data
    
def refresh_prices():
    config_data = read_local_json("config.json")
    companies_data = config_data["companies"]

    table_data = {}
    table_data["stocks"] = {}
    for stock in companies_data:
        table_data["stocks"][stock] = calculate_prices(stock)
    table_data["next_round"] = len(table_data["stocks"][stock])

    write_local_json("table.json", str_round_table_data(table_data))


def leading_stock():
    table_data = read_local_json("table.json")
    next_round = table_data["next_round"]
    stocks_table = table_data["stocks"]
    stock_candidate = ""
    max_price = -1
    for stock in stocks_table:
        price = float(stocks_table[stock][next_round-1])
        if price >= max_price:
            max_price = price
            stock_candidate = stock
    return stock_candidate


def read_config():
    return read_local_json("config.json")

def read_table():
    return read_local_json("table.json")