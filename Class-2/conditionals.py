x=5
y=6

print(x>6)
print(y<10)

print((x>4) and (y==6))
print((x>4) and (y!=6))

print(not((x>10) and (y==6)))

if x>4 and y<10:
    print("Correct")

if x>6 or y<10:
    print("Correct")    

if x>6 and y<10:
    print("Correct")
elif x==5 and y==6:
    print("Hello")      
else:
    print("World")      

    