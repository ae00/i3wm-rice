import datetime

fixed_holidays = [
	("Nyårsdagen", (1,1)),
	("Trettondedag jul", (1,6)),
	("Långfredagen", (4,18)),
	("Påskafton", (4,19)),
	("Påskdagen", (4,20)),
	("Annandag påsk", (4,21)),
	("Första Maj", (5,1)),
	("Kristi himmelsfärdsdag", (5,29)),
	("Sveriges nationaldag", (6,6)),
	("Pingstdagen", (6,8)),
	("Annandag pingst", (6,9)),
	("Midsommarafton", (6,20)),
	("Midsommardagen", (6,21)),
	("Alla helgons dag", (11,1)),
	("Julafton", (12,24)),
	("Juldagen", (12,25)),
	("Annandag jul", (12,26)),
	("Nyårsafton", (12,31))
]

def get_next_holiday():
    today = datetime.date.today()
    current_year = today.year

    holidays_this_year = []

    for holiday_name, holiday_date in fixed_holidays:
        month, day = holiday_date
        holiday_date = datetime.date(current_year, month, day)
        if holiday_date >= today:
            holidays_this_year.append((holiday_name, holiday_date))

    next_holiday_name, next_holiday_date = min(holidays_this_year, key=lambda x: x[1])
    days_left = (next_holiday_date - today).days
    weekday = next_holiday_date.strftime('%A')

    return next_holiday_name, next_holiday_date, days_left, weekday

holiday_name, holiday_date, days_left, weekday = get_next_holiday()

print(f"{holiday_name}, {holiday_date} - {weekday} - {days_left} days.")
