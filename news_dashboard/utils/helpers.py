from datetime import datetime


def format_date(date_string):
    try:
        return datetime.strptime(
            date_string,
            "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%d %b %Y %I:%M %p")
    except:
        return date_string