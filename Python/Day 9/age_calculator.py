import datetime
birth_date= int(input("enter the birth year "))
current_year=datetime.datetime.now().year
print(f"{current_year-birth_date}")