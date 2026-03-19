def check_position(api, symbol):

    positions = api.list_positions()

    for position in positions:
        if position.symbol == symbol:
            return True

    return False


# Later you can add:

# stop loss

# portfolio limits

# max trades per day