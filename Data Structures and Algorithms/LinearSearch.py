def linearSearch(Arr, key):
    for i in range(0, len(Arr)):
        if(Arr[i] == key):
            print("Found at:", i + 1)

# Initialize and empty list
lst = [43, 12, 45, 90, 2, 54, 1, 45]

# n = int(input("Number of elements: "))

# for i in (0, n):
#     ele = int(input())
#     lst.append(ele)

linearSearch(lst, 45)