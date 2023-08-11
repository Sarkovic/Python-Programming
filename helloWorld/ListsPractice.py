# Methods and functions related to Lists


bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles)

# Print the elements of the list in Title Case
for x in bicycles:
    print(x.title())

names = ['Rahim', 'Karim', 'Suzana', 'Ashek', 'Huda']

for x in names:
    print(f"Hello {x}, you look great today!")

print('\n')
print(names)
names[0] = 'Tanjiro'
print(names)
# Append method will add a new element at the end of the list
names.append('Nezuko')
print(names)
# Insert method will add a new element in the given index
names.insert(0, 'Genichiro')
print(names)

print('\n')
# Pop method will remove the last index in the list
popped_value = names.pop()
print(popped_value)
print(names)
# Pop method with index as argument will remove an element from any
# position in a list
popped_value = names.pop(3)
print(popped_value)
print(names)
# Remove method will remove the first occurrence of the element
# that matches with the value specified. If there are multiple
# element with the same value then we need to use a loop to remove those
# Removing an item by value
names.remove('Ashek')
print(names)

# List organizing
print('\n')

cars = ['bmw', 'audi', 'toyota', 'porsche', 'subaru', 'lamborghini', 'nissan']

# In order to maintain the order of the list but present it in a sorted
# order, we can use the sorted() function which can also be used for reverse
print(f"Original list: {cars}")
print(f"Sorted list: {sorted(cars)}")
print(f"Reverse sorted list: {sorted(cars, reverse=True)}")
print(f"Let's see if it remains to the original state:\n{cars}")

# Permanent sort with the sort method
cars.sort()
print(cars)
# Permanent Reverse sort
cars.sort(reverse=True)
print(cars)

# Reverse method doesn't sort backward alphabetically rather it reverses
# the default order of the list, the way we wrote/gave input in the list
bikes = ['suzuki', 'ducati', 'bmw', 'indian', 'yamaha', 'honda']
print(bikes)
bikes.reverse()
print(bikes)

# Length of the list
print(len(bikes))

for bike in bikes:
    print(f"{bike.title()} is great!!")

pizzas = ['pepperoni pizza', 'four seasons pizza', 'cheese pizza']

for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really love pizza!")

animals = ['dog', 'cat', 'rabbit', 'hamster']

for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")

numbers = list(range(0, 11, 2))
print(numbers)

squares = []
for value in range(1, 11):
    # square = value ** 2
    squares.append(value ** 2)

print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))

squares_two = [value ** 3 for value in range(1, 11)]
print(squares_two)

one_million = list(range(1, 1000000))
print(sum(one_million))

burgers = ['chicken', 'beef', 'cheese', 'naga', 'sausage', 'ginger']
print("The first three items in the list are:")
print(burgers[:3])
print("The items from the middle of the list are:")
print(burgers[1:4])
print("The last three items in the list are:")
print(burgers[-3:])

friend_burgers = burgers[:]

print(friend_burgers)

burgers.append('bbq chicken')
print(burgers)
friend_burgers.append('spicy beef')
print(friend_burgers)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Although we cannot modify a tuple, we can assign a new value to a
# variable that represents  a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)


# Dictionaries
alien_0 = {'color': 'green',
           'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

# adding new key-value pair in a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

person = {
    'first_name': 'Sadi',
    'last_name': 'Rahman',
    'age': 23,
    'city': 'Dhaka'
}

print(person)

favorite_color = {
    'Subhey': 'Black',
    'Nodi': 'Green',
    'Konku': 'Red',
    'Megho': 'Pink',
    'Aungshu': 'Blue'
}

for name, color in favorite_color.items():
    print(f"Key: {name}")
    print(f"Value: {color}\n")

print(favorite_color.keys())
print(favorite_color.values())

# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'blue', 'points': 9}
alien_2 = {'color': 'red', 'points': 4}

print(f"{(22/7): .5f}")