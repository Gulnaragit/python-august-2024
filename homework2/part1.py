years = int(input("Enter number of years: "))
days=years*365
weeks=years*52
months=years*12
hours=years*days*24

def day():
    print(f"In {years} years there are {days} days")
day()

def week():
    print(f"In {years} years there are {weeks} weeks")
week()

def month():
    print(f"In {years} years there are {months} month")
month()

def hour():
    print(f"In {years} years there are {hours} hours")
hour()
