from datetime import datetime
def today_to_file():
    today = (datetime.today()).strftime("%Y_%#m_%#d")
    return today
