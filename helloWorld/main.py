import math
import time

# first_value = second_value = third_value = 44
# print(first_value)
# print(second_value)
# print(third_value)
# first_value, second_value, third_value = "Stringiii", 13, True
# print(first_value, second_value, third_value)
# print(first_value.find("i"))
# print(first_value.upper())
# print(first_value.lower())
# print(first_value.isalpha())
# print(first_value.count("i"))
# print(first_value.replace("i", "a"))
# print(first_value*5, end=", ")

# name = input("What is your name?\n")
# age = int(input("How old are you?\n"))
# height = float(input("What is your height?\n"))
# age += 1
# print("Hello " + name)
# print("Your age is: " + str(age))
# print("Your height is " + str(height))

# Math Operations:
# pi = -3.14
# x = 1
# y = 2
# z = 3
# print(max(x, y, z))
# print(min(x, y, z))
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(420)

# String Slicing:
# name = "Bro Code"
# first_name = name[0:3]
# last_name = name[4:8]
# funky_name = name[::2]
# print(first_name)
# print(last_name)
# print(funky_name)
# reversed_name = name[::-1]
# print(reversed_name)
#
# website = "http://google.com"
# website2 = "http://wikipedia.com"
#
# slice = slice(7, -4)
# print(website[slice])
# print(website2[slice])

# IF/ELSE:
# age = int(input("What is your age?: "))
#
# if 13 <= age <= 19:
#     print("You are a teen")
#     name = input("What is your name?: ")
#     print("Hello " + name)
#     print("How are you, " + name + "?\nEverything alright?")
# elif 20 <= age <= 30:
#     print("You are in your youth!")
# elif 31 <= age <= 50:
#     print("You are experiencing midlife crisis.")
# elif age == 100:
#     print("You are century old")
# else:
#     print("You are old")

# Loops

# name = input("What is your name?: ")
# while len(name) == 0:
#     name = input("What is your name?: ")
#
# count = 0
# while count <= 10:
#     print(count)
#     count += 1

# print("\n")
#
# for i in range(5, 10+1, 2):
#     print(i)
#
# print("\n")
# for i in "Bro Code":
#     print(i)
#
# print("\n")
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)  # Waits for 1 second to print the next
# print("Happy New Year")

# Nested Loops:
# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end=" ")
#     print()

# Loop control statements:
# while True:
#     name = input("Enter your name: ")
#     if len(name) != 0:
#         break
#
# phone_number = "123-456-789"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(20):
#     if i == 13:
#         continue
#     print(i+1)
#
# print("\n")
# for i in range(20):
#     if i == 13:
#         pass
#     else:
#         print(i+1)

# List:
# food = ["pizza", "hamburger", "hotdog", "spaghetti", "noodles", "pizza"]
# food[0] = "sushi"
# food[1] = 245
# food[3] = 2435.456
#
# # print(food.count("pizza"))
# # food.append("pizza")
# # food.append("Fried Rice")
# # food.remove("pizza")
# # food.remove("noodles")
# # food.remove("hotdog")
# # food.insert(0, "cake")
#
# for i in food:
#     print(i)

# 2D Lists

drinks = ["coffee", "soda", "tea"]
dinner = ["rice", "meat", "vegetable"]
dessert = ["icecream", "cake"]

food = [drinks, dinner, dessert]

for i in food:
    print(i)

print("\n")
for i in food:
    for j in i:
        print(j, end=" ")
    print()
