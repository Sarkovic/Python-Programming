# List
my_list = ["Salma", "Ratan", "Mim", 123, True]
print(my_list)
print(len(my_list))
print(type(my_list))


if "Salma" in my_list:
  print("Yes")
else:
  print("No")

print(my_list)

# Show values from the back
print(my_list[-3])

my_list.append("CSE")
print(my_list)

my_list.insert(1, 3.5)
print(my_list)

x = my_list.pop()
print("Popped value: " + str(x))
print(my_list)

my_list.remove("Salma")

a = [1, 2, 3]
print(a + a)
print(a * 3)