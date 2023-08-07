# 1
def pattern_one():
    n = int(input())
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end="")
        print()


# 2. 3 -> 123
#         234
#         345
#    4 -> 1234
#         2345
#         3456
#         78910
def pattern_two():
    n = int(input())
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            print(j, end="")
        print()


# 3. 3 -> 1
#         23
#         345
def pattern_three():
    n = int(input())
    for i in range(n):
        # Store i value in another variable k
        k = i
        # The loop will continue till i so that it
        # print 1 digit in first line, 2 digits in second and so on...
        for j in range(i + 1):
            # Here i is starting from 0, but we do not have
            # 0 in our pattern so, k + 1
            print(k + 1, end="")
            # incrementing k separately to match the pattern
            k += 1
        print()


# pattern_one()
# pattern_two()
# pattern_three()
