
values = [1, 2, "rahul", 4, 5]
# List is data type that allows multiple values and can be different data types

print(values[0])  # 1

print(values[3])  # 4
print(values[-1])  #5
print(values[1:3])  # 2 rahul
values.insert(3, "shetty")   #[1, 2, 'rahul', 'shetty', 4, 5]
print(values)
values.append("End")  #[1, 2, 'rahul', 'shetty', 4, 5, 'End']
print(values)

values[2] = "RAHUL" #Updating

del values[0]

print(values)
del values[2]
print(values)
# Tuple - Same as LIST Data type but immutable
val = (1, 2, "rahul", 4.5)

print(val[1])

#val[2] = "RAHUL"

print(val)

# Dictionary
dic = {"a": 2, 4:"bcd", "c": "Hello world"}

print(dic[4])
print(dic["c"])

#
dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "shetty"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])

print("i am changing it for my git example")
print("another line for the same")


print ("branch demo")
print("second line in branch demo")

print("pushed now to gitstuff demo")















