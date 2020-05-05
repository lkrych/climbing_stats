from datetime import datetime

def get_query_timestamps(filter):
    today = datetime.now()
    today_timestamp = datetime.timestamp(today)
    from_timestamp = ""

    if filter == "month" or not filter:
        current_month = today.replace(day=1)
        from_timestamp = datetime.timestamp(current_month)
    elif filter == "year":
        current_year = today.replace(month=1, day=1)
        from_timestamp = datetime.timestamp(current_year)
    return from_timestamp, today_timestamp