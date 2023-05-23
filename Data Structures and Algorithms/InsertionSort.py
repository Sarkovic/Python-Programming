def insertionSort(A):
    for step in range(1, len(A)):
        key = A[step]
        j = step - 1

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1

        A[j + 1] = key

# Initialize an empty list
arr = []

n = int(input("Number of elements: "))

for i in range(0, n):
    ele = int(input())
    # Adding the element
    arr.append(ele)

# Print the unsorted list
print(arr)

insertionSort(arr)
# Print the sorted list
print(arr)