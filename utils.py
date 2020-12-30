from datetime import datetime

new_year = datetime.now().year + 1


def count_down() -> tuple:
    """ Function return days and time to next new year"""

    new_year = datetime(datetime.now().year + 1, 1, 1)
    today = datetime.now()

    day_diff = new_year.day - today.day
    if day_diff < 0:
        day_diff = 30 + new_year.day - today.day
    month_diff = 12 - today.month
    total_days = int(
        day_diff + ((month_diff / 2) * 30) + ((month_diff / 2) * 31)
    )

    hour_diff = new_year.hour - today.hour
    if hour_diff < 0:
        hour_diff = (new_year.hour - today.hour) + 23

    minute_diff = new_year.minute - today.minute
    if minute_diff < 0:
        minute_diff = 59 + new_year.minute - today.minute

    sec_diff = new_year.second - today.second
    if sec_diff < 0:
        sec_diff = 59 + (new_year.second - today.second)

    return (
        str(total_days).zfill(2),
        str(hour_diff).zfill(2),
        str(minute_diff).zfill(2),
        str(sec_diff).zfill(2),
    )
