# def moving_average_strategy(data):
#     if len(data) < 30:
#         return "HOLD"

#     data['short_ma'] = data['Close'].rolling(10).mean()
#     data['long_ma'] = data['Close'].rolling(30).mean()

#     latest = data.iloc[-1]

#     if latest['short_ma'] > latest['long_ma']:
#         return "BUY"
#     elif latest['short_ma'] < latest['long_ma']:
#         return "SELL"

#     return "HOLD"

def improved_strategy(data, position=None):
    print("Running improved strategy position:", position)

    # Indicators
    data = data_indicators(data)
    latest = data.iloc[-1]
    current_price = latest['close']

    print("Calculated moving averages. Latest long MA:", latest['long_ma'], "Latest short MA:", latest['short_ma'])
    print("Latest Close Price:", latest['close'])
    print("Latest RSI:", latest['rsi'])

    # ---------------------------
    # TREND CONFIRMATION
    # ---------------------------
    uptrend = (
        latest['close'] > latest['long_ma'] and
        latest['long_ma'] > latest['ma200']
    )

    # -------------------------------
    # CASE 1: NO POSITION → LOOK TO BUY
    # -------------------------------
    if position is None:

        if (
            uptrend and   # trend up
            latest['close'] > latest['short_ma'] and
            30 < latest['rsi'] < 50                  # pullback zone (better than <40)
        ):
            return "BUY"

        return "HOLD"

    # -------------------------------
    # CASE 2: ALREADY HOLDING → MANAGE TRADE
    # -------------------------------
    else:
        buy_price = float(position.avg_entry_price)
        print("Current Price:", current_price)
        print("Buy Price:", buy_price, "first condition:", buy_price * 0.97, "second condition:", buy_price * 1.04)
        # Stop-loss (protect downside)
        if current_price < buy_price * 0.97:   # 3% loss
            return "SELL"

        # Take-profit (lock gains)
        if current_price > buy_price * 1.04:   # 4% gain
            return "SELL"

        # Exit if trend weakens
        if latest['close'] < latest['short_ma']:
            return "SELL"

        return "HOLD"

def get_strategy_data(data, position):
    """
    Returns strategy data with RSI values
    """
    print("Running strategy get_strategy_data...")
    # Call your existing strategy function or data retrieval logic
    data = improved_strategy(data, position)
    print("Strategy signal:", data)
    return data

def data_indicators(data):
    data['short_ma'] = data['close'].rolling(20).mean()
    data['long_ma'] = data['close'].rolling(50).mean()
    data['ma200'] = data['close'].rolling(200).mean()

    from ta.momentum import RSIIndicator
    data['rsi'] = RSIIndicator(data['close'], window=14).rsi()

    return data


# You can later add strategies like:
# RSI
# Bollinger Bands
# Breakout trading

# New fixes of improved_strategy:

# | Problem         | Fix                |
# | --------------- | ------------------ |
# | Too many trades | RSI filter         |
# | False signals   | Trend filter       |
# | Big losses      | Stop-loss          |
# | Noise trading   | Confirmation rules |
