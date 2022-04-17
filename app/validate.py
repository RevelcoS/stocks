from app.errors import ActionsTableValidationError
from app import ConfigHandler

def validate_action(string):
    '''string must be in format "<+/-/0> <station>"'''
    is_valid, msg = True, "OK"
    config_data = ConfigHandler.read_data()
    available_signs = config_data["algorithm"]["available_signs"]
    available_stations = config_data["available_stations"]
    args = string.split()
    if len(args) != 2:
        msg = f"action '{string}' must be in format '<+/-/0> <station>'"
        raise(ActionsTableValidationError(msg))
    
    sign, station = args
    if sign not in available_signs:
        msg = f"'{sign}' is not in available signs: {available_signs}"
        raise(ActionsTableValidationError(msg))
    
    if station not in available_stations:
        msg = f"'{station}' is not in available stations: {available_stations}"
        raise(ActionsTableValidationError(msg))

    return (is_valid, msg)

def validate_actions_table(table):
    is_valid, msg = True, "OK"
    
    config_data = ConfigHandler.read_data()
    max_rounds = config_data["max_rounds"]

    # Validate the keys
    keys = list(table.keys())
    available_keys = map(str, range(1, max_rounds))
    for key in keys:
        if key not in available_keys:
            is_valid = False
            break
    
    if not is_valid:
        msg = f"key '{key}' is invalid"
        raise(ActionsTableValidationError(msg))

    # Validate the rounds ordering
    rounds = sorted(map(int, keys))
    if len(rounds) != 0 and rounds[0] != 1:
        is_valid = False
        msg = f"first round should start from '1'"
        raise(ActionsTableValidationError(msg))
    
    for idx in range(1, len(rounds)):
        if rounds[idx] - rounds[idx-1] != 1:
            is_valid = False
            break
    
    if not is_valid:
        msg = f"round '{rounds[idx-1]+1}' is missed"
        raise(ActionsTableValidationError(msg))
    
    # All of the values must be lists
    vals = list(table.values())
    for val in vals:
        if type(val) != list:
            is_valid = False
            break
    
    if not is_valid:
        msg = f"all values must be lists ({val} is not a list)"
        raise(ActionsTableValidationError(msg))
    
    # All list elements must be strings
    for lst in vals:
        for element in lst:
            if type(element) != str:
                is_valid = False
                break
    
    if not is_valid:
        msg = f"all list values must be strings ({element} is not a string)"
        raise(ActionsTableValidationError(msg))
    
    # Validate actions
    for lst in vals:
        for action in lst:
            validate_action(action)

    return (is_valid, msg)