years = int(input("Enter number of years: "))

def day():
    print(f"In {years} years there are {years*365} days")
day()

def week():
    print(f"In {years} years there are {years*52} weeks")
week()

def month():
    print(f"In {years} years there are {years*12} month")
month()

def hour():
    print(f"In {years} years there are {years*365*24} hours")
hour()
