age = int(input("Enter your age: "))

if age >=13 and age <18:
    print("Teenager")
elif age >=18 and age <65:
    print("Adult")
elif age >=65:
    print("Elder")
else:
    print("Enter correct age.")            


tip = int(input("Enter your tip: "))

if tip == 15:
    print("Standard")
elif tip == 18:
    print("Good")
elif tip >= 20:
    print("My hero")
else:
    print("Enter correct tip amount.") 