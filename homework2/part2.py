a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
oper = input("Choose an operator +, -, *, / : ")

if oper == "+" :
    def add():
        return(a + b)
    print(add())
elif oper == "-" :
    def subt():
        return(a - b)
    print(subt())  
elif oper == "*" :
    def mult():
        return(a * b)
    print(mult())  
elif oper == "/" :
    def div():
        return(a / b)
    print(div())        
else:
    print("Incorrect entry.")