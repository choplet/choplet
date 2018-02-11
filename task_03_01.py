
from datetime import date
def deadlinedate(n):
    today = date.today()
    
    deadline = date(today.year,today.month, today.day+n)

    return deadline

print(deadlinedate(1))