from datetime import date
from datetime import datetime

def calculate_age(born):
    born = datetime.strptime(born, '%d/%m/%Y')
    today = date.today()
    try: 
        birthday = born.replace(year = today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year = today.year, month=born.month+1, day=1)
    if not birthday.year > today.year:
        return today.year - born.year - 1
    else:
        return today.year - born.year
    
print(datetime.now().strftime("%d_%m_%Y %H:%M:%S"))