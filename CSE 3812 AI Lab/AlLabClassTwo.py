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

for i in my_list:
    print(i)

print()

for i in range(len(my_list)):
    print(my_list[i])

print()

graph = [[0, 1, 1, 1, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 1, 1, 0]]

# print(len(graph))

vertex = ['A', 'B', 'C', 'D', 'E']

for i in range(len(graph)):
    print(vertex[i], " -> ")
    for j in range(len(graph)):
        if graph[i][j] == 1:
            print(vertex[j])

print("\n")

# Set

set_one = {"apple", "banana", 1, "apple", True}
print(set_one)

set_one.add("mango")
print(set_one)

set_two = {"yellow", "banana"}
set_one.update(set_two)
print(set_one)

set_one.remove("yellow")
print(set_one)

print("\n")
for i in set_one:
    print(i)

print("\n")

# Tuple
# We can't insert or delete item in
# a tuple. Convert to list then add
tuple_one = ("Hello", 456, "World", "Cat", False)
tuple_two = ("Green", "Yellow")

x = list(tuple_one)
x.append("Magenta")
tuple_one = tuple(x)
print(tuple_one)


# Tuple unpacking
thisTuple = (1, "apple", True, [1, 2])
*x, y = thisTuple
print(x, y)

x, *y = thisTuple
print(x, y)

print("\n")
# Dictionary
person = {
    "name": "Subhey Sadi Rahman",
    "email": "srahman212074@bscse.uiu.ac.bd",
    "joined": 2019,
    "course": ["SPL", "AI", "DSA"]
}

# prints the keys along with the values
print(person)
# Only prints the keys
print(person.keys())
# Only prints the values
print(person.values())

# Will only print the value of "joined"
print(person.get("joined"))

# Print the dictionary keys and values in a loop
for key in person:
    print(key, "->", person[key])


# freq_count will count the highest frequency of a character in a string
def freq_count():
    sentence = list("Dhaka is our Capital")
    frq = 0
    for i in range(len(sentence)):
        cnt = 0
        for j in range(len(sentence)):
            if sentence[i] == sentence[j]:
                cnt += 1
        if frq < cnt:
            frq = cnt
    print(frq)


print(freq_count())

# Prints the graph
graph_two = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["A", "B", "E"],
    "E": ["C", "D"]
}

for key in graph_two:
    print(key, "-->", graph_two[key])

