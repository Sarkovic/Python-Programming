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
