# vstupom z klavecnice zadat nejaky datum a nasledne vypocitas kolko rokov, mesiacov, dni, hodin, minut a sekund preslo od daneho datumu (po aktualny datum)
import datetime

def calc_time_duration(input_date):
    # parse input date
    try:
        date = datetime.datetime.strptime(input_date, "%Y-%m-%d")

        # get date-time now:
        now = datetime.datetime.now()

        difference = now - date   #returns different in days and hours, minutes and seconds

        # Calculate years, months, and days
        years = difference.days // 365          #we calculate from days difference.days
        months = (difference.days % 365) // 30
        days = (difference.days % 365) % 30

        # calculate  time (we start from getting total difference in seconds)
        total_seconds = difference.seconds

        # calculate H,M,S
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = (total_seconds %3600) % 60

        return years, months, days, hours, minutes, seconds
    except ValueError or TypeError:
        print("Wrong format of a date")


input_date = input("Insert any date in format: 'yyyy-mm-dd': ")
years, months, days, hours, minutes, seconds = calc_time_duration(input_date)
print(f"difference is: {years} years, {months} months, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
