from datetime import datetime, timedelta

def convDate(date):
    try:
        date_ = datetime.strptime(date[:-7], "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        date_ = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    return date_

def genOHLC(timeframe, data):
    """
    data: {
        "dates": List<DateTime object>,
        "prices": List<Float object>,
        "volumes": List<Int object>
    }
    """

    groups = []

    dates_ = iter(data["dates"])
    for date in dates_:
        cur = convDate(date)
        count = 0

        group = []
        group.append([date, data["prices"][data["dates"].index(date)], data["volumes"][data["dates"].index(date)]])

        for sub_date in dates_:
            if cur + timedelta(minutes=timeframe) > convDate(sub_date):
                group.append([sub_date, data["prices"][data["dates"].index(sub_date)]])
                count += 1
            else:
                break

        groups.append(group)

    ohlc = {
        "open": [],
        "high": [],
        "low": [],
        "close": [],
        "volume": [],
        "dates": []
    }

    for group in groups:
        open = group[0][1]
        high = float("-inf")
        low = float("inf")
        close = group[-1][1]
        date = group[0][0]
        volume = group[0][2]

        for point in group:
            if point[1] > high:
                high = point[1]
            if point[1] < low:
                low = point[1]

        ohlc["open"].append(open)
        ohlc["high"].append(high)
        ohlc["low"].append(low)
        ohlc["close"].append(close)
        ohlc["volume"].append(volume)
        ohlc["dates"].append(date)

    return ohlc
