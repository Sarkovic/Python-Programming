# 1. Program that will print upto Nth terms
def print_upto_n(n):
    for i in range(n):
        print(i + 1)


# 2. Program that will print odd numbers up to Nth terms
def print_odd(n):
    count = 0
    i = 1
    while count != n:
        print(i)
        i += 2
        count += 1


# 3. Print 1/0 series upto Nth terms
def print_one_zero(n):
    count = 0
    i = 1
    while count != n:
        if i % 2 == 1:
            print(1)
        else:
            print(0)
        i += 1
        count += 1


# 4. Program that will take N numbers as inputs and compute their average.
def avg_of_inputs(n):
    sum_of_inputs = 0
    for i in range(n):
        sum_of_inputs += float(input())
    print(sum_of_inputs / n)


# 5. Program that will take two numbers X and Y as inputs
#    Then it will print the square of X and increment (if X<Y)
#    or decrement (if X>Y) X by 1, until X reaches Y.
#    If and when X is equal to Y, the program prints “Reached!”
def x_and_y():
    x, y = map(int, input().split())
    while x != y:
        if x < y:
            print(x ** 2, end=", ")
            x += 1
        else:
            print(x ** 2, end=", ")
            x -= 1
    print("Reached!")


# 6. Player-1 picks a number X and Player-2 has to guess that number within N tries.
# For each wrong guess by Player-2, the program prints “Wrong, N-1 Choice(s) Left!”
# If Player-2 at any time successfully guesses the number,
# the program prints “Right, Player-2 wins!” and terminates right away.
# Otherwise, after the completion of N wrong tries,
# the program prints “Player-1 wins!” and halts.
def number_guessing():
    x = int(input("Pick a number: "))
    n = int(input("Enter number of tries: "))
    for i in range(n):
        # Input values of guesses
        guess = int(input())
        if guess == x:
            print("Right, Player - 2 wins!")
            break
        else:
            # Decrement the values of tries left
            n -= 1
            print("Wrong,", n, "Choice(s) left!")
            continue

    # If no tries are left then player - 1 wins
    if n == 0:
        print("Player - 1 wins!")


# 7. Program that will run and show keyboard inputs
#    until the user types an "A" at the keyboard.
def detect_a():
    user_input = input("Enter your input: ")
    i = 1
    while user_input != 'A':
        print("Input " + str(i) + ":", user_input)
        user_input = input("Enter your input: ")
        i += 1


# 8. Program that will reverse the digits of an input integer.
def reverse_digits():
    n = int(input("Enter an integer number: "))
    rev = 0
    while n != 0:
        rev *= 10
        rev += n % 10
        n //= 10

    print(rev)


# 9. Program that will find the grade of N students
def grade_output():
    n = int(input("Enter the number of students: "))
    for i in range(n):

        # Marks can be in float values
        attendance, assignment, class_test, mid, final = map(float, input().split())

        # Convert the total number out of 100
        total = ((attendance + assignment + class_test + mid + final) * 100) / 180

        # print("Total is: ", total)

        # Grade determiner
        if total >= 90:
            print("Student " + str(i + 1) + " : A")
        elif 86 <= total <= 89:
            print("Student " + str(i + 1) + " : A-")
        elif 82 <= total <= 85:
            print("Student " + str(i + 1) + " : B+")
        elif 78 <= total <= 81:
            print("Student " + str(i + 1) + " : B")
        elif 74 <= total <= 77:
            print("Student " + str(i + 1) + " : B-")
        elif 70 <= total <= 73:
            print("Student " + str(i + 1) + " : C+")
        elif 66 <= total <= 69:
            print("Student " + str(i + 1) + " : C")
        elif 62 <= total <= 65:
            print("Student " + str(i + 1) + " : C-")
        elif 58 <= total <= 61:
            print("Student " + str(i + 1) + " : D+")
        elif 55 <= total <= 57:
            print("Student " + str(i + 1) + " : D")
        else:
            print("Student " + str(i + 1) + " : F")


# 10. Sum of the following series: 1, -2, 3, -4, 5, -6, 7, -8, 9, -10
def sum_of_pos_neg():
    n = int(int(input("Enter the value of N: ")))
    total = 0
    for i in range(n + 1):
        if i % 2 == 1:
            total += i
        else:
            total -= i
    print("Result:", total)


# 11. Program that will calculate the following series: 1^2.2 + 2^2.3 + 3^2.4 + 4^2.5 + ……
def sum_sqr_mult():
    n = int(input("Enter the value of N: "))
    total = 0
    for i in range(n + 1):
        total += ((i ** 2) * (i + 1))
    print("Result:", total)


# 12. Fibonacci
def fib():
    n = int(input())
    # Initializing the 0 and 1 index of the list,
    # dynamic programming concept
    arr = [1, 1]
    # Base case
    if n <= 1:
        print(n)
    else:
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])
        print(arr)


# 13. Factorial
def factorial(n):
    # Starting loop from N - 1 and decrementing it till 1
    for i in range(n - 1, 1, -1):
        # Multiplying with existing value of N
        n *= i
    return n


# 14. Combinations Formula
def combinations():
    n, r = [int(x) for x in input().split()]
    res = factorial(n) / (factorial(r) * factorial(n - r))
    print(res)


# 15. x to the power y
def x_pow_y():
    x, y = [int(x) for x in input().split()]

    if y == 0:
        print(1)
    else:
        for i in range(y - 1):
            x *= x
        print(x)


# 16. GCD and LCM of two positive integers
def gcd_lcm():
    num_one, num_two = map(int, input().split())

    # Finding the GCD (Greatest Common Divisor) / HCF (Highest Common Factor)
    if num_one < num_two:
        gcd = num_one
    else:
        gcd = num_two

    while gcd > 0:
        if num_one % gcd == 0 and num_two % gcd == 0:
            break
        gcd -= 1

    # Finding the LCM (Least Common Multiple) by dividing the
    # multiplication of two numbers. Reference: [a * b = gcd(a,b) * lcm(a,b)]
    lcm = (num_one * num_two) // gcd

    print("GCD: " + str(gcd) + "\n" + "LCM: " + str(lcm))


# 17. Prime number identifier
def prime_number():
    n = int(input())
    flag = 0
    for i in range(n - 1, 2, -1):
        if n % i == 0:
            flag = 1
    if flag == 1 or n == 1:
        print("Not prime")
    else:
        print("Prime")


# 18. Palindrome
def palindrome():
    n = int(input())

    # Store the value of N as we will be changing it in
    # the reverse digits section
    temp = n

    # Reverse digits
    rev = 0
    while n != 0:
        rev *= 10
        rev += n % 10
        n //= 10

    # Checking
    if temp == rev:
        print("Yes")
    else:
        print("No")


# 20. program that takes an integer number n as input
# and find out the sum of the following series up to n terms.
# 1 + 12 + 123 + 1234 +....
def sum_of_digits_and_series():
    n = int(input())

    # initialize two variables to store values
    total = 0
    series_total = 0

    for i in range(1, n + 1):
        # Multiplying with 10 will shift left and
        # create an empty spot 0 in the Ones position
        total *= 10
        # Adding i will replace ones position with the iterated value
        total += i
        # Then add the total values in the series total
        series_total += total
    print(series_total)

# Driver Code
# N = int(input("Enter the value of N: "))
# print_upto_n(N)
# print_odd(N)
# print_one_zero(N)
# avg_of_inputs(N)
# x_and_y()
# number_guessing()
# detect_a()
# reverse_digits()
# grade_output()
# sum_of_pos_neg()
# sum_sqr_mult()
# fib()
# x_pow_y()
# print(factorial(N))
# combinations()
# prime_number()
# gcd_lcm()
# palindrome()
# sum_of_digits_and_series()
