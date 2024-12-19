a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
oper = input("Choose an operator +, -, *, / : ")

if oper == "+" :
    def sum():
        return(a + b)
    print(sum())
elif oper == "-" :
    def sum():
        return(a - b)
    print(sum())  
elif oper == "*" :
    def sum():
        return(a * b)
    print(sum())  
elif oper == "/" :
    def sum():
        return(a / b)
    print(sum())        
else:
    print("Incorrect entry.")