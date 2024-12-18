foods = ("apple", "banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry") 
calories = (52, 96, 62, 605, 33, 68, 50, 33)
print(foods)
print(calories)

foods_list = list(foods)    #print(list(foods))
cal_list = list(calories)   #print(list(calories))
print(foods_list)
print(cal_list)

print(foods_list[4], cal_list[4])

print(foods_list[-2], cal_list[-2])

foods_set = set(foods)  #print(set(foods))
print(foods_set)

foods_dict = {"apple" : 52, "banana" : 96, "orange" : 62, "mango" : 605, "strawberry" : 33, "grape" : 68, "mandarin" : 50, "strawberry" : 33} 

foods_dict["tomato"] = 60 
print(foods_dict)

foods_dict["tomato"] = 50 
print(foods_dict)

print(foods_dict["apple"] + foods_dict["banana"])

# how to convert list to dictionary or otherway around.