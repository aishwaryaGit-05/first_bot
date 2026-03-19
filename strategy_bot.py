def moving_average_strategy(data):
    if len(data) < 30:
        return "HOLD"

    data['short_ma'] = data['Close'].rolling(10).mean()
    data['long_ma'] = data['Close'].rolling(30).mean()

    latest = data.iloc[-1]

    if latest['short_ma'] > latest['long_ma']:
        return "BUY"
    elif latest['short_ma'] < latest['long_ma']:
        return "SELL"

    return "HOLD"



# You can later add strategies like:

# RSI

# Bollinger Bands

# Breakout trading