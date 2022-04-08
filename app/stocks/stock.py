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
    info_data = read_local_json("info.json")
    log_data = read_local_json("log.json")
    teams_data = read_local_json("teams.json")

    prices = [6]
    percent = 15
    for round in range(1, len(log_data)+1):
        coeff = 1
        for action in log_data[str(round)]:
            team, passed, station, = action.split()
            if station in info_data[stock]:
                bool_passed = ("+" == passed)
                bool_active_stock = (stock in teams_data[team])
                if (bool_passed == bool_active_stock):
                    coeff *= 1 + percent / 100
                else:
                    coeff *= 1 - percent / 100

        prices.append(prices[-1] * coeff)

    return prices


def format_table_data(table_data):
    stocks_table = table_data["stocks"]
    for stock in stocks_table:
        for round in range(len(stocks_table[stock])):
            stocks_table[stock][round] = format(stocks_table[stock][round], ".2f")
    return table_data
    
def refresh_prices():
    info_data = read_local_json("info.json")

    table_data = {}
    table_data["stocks"] = {}
    for stock in info_data:
        table_data["stocks"][stock] = calculate_prices(stock)
    table_data["next_round"] = len(table_data["stocks"][stock])

    write_local_json("table.json", format_table_data(table_data))


def leading_stock():
    table_data = read_table()
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

def read_table():
    return read_local_json("table.json")