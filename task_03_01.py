import time
from datetime import date
def get_days_to_new_year():
    today = date.today()
    today
    
    new_year = date(today.year, 12, 31)
    
    time_to_new_year = abs(new_year - today)