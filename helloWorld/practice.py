class PracticeFunctions:
    # Recursive funtion to check Even or Odd
    def checkevenodd(self, n):
        if n < 2:
            return n % 2 == 0
        return self.checkevenodd(n - 2)

    # Check positive or negative
    def checkposneg(self, n):
        if n < 0:
            print("Negative")
        else:
            print("Positive")

    # Check Palindrome
    def checkpalindrome(self, n):
        temp = n
        rev = 0
        while n > 0:
            dig = n % 10
            rev = rev * 10 + dig
            n = n // 10
        if(temp == rev):
            print("Palindrome")
        else:
            print("Not Palindrome")

    # Reverse a number
    def reverse(self, n):
        rev = 0
        while n > 0:
            dig = n % 10
            rev = rev * 10 + dig
            n = n // 10
        return rev

    # Not divisible by either 2 or 3
    def divbytwothree(self, n):
        for i in range(0, n + 1):
            if i % 2 != 0 and i % 3 != 0:
                print(i)

    # Divisible by 7 and Multiple of 5 in a Given Range
    def divbysevenmultoffive(self, start, end):
        for i in range(start, end + 1):
            if i % 7 == 0 and i % 5 == 0:
                print(i)

    def sumofdigits(self, n):
        sum = 0
        while n > 0:
            sum += n % 10
            n = n // 10
        return sum


obj = PracticeFunctions()

num = int(input("Enter number: "))

print(obj.sumofdigits(num))

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
#
# obj.divbysevenmultoffive(start, end)

# obj.divbytwothree(num)

# print(obj.reverse(num))

# if obj.checkevenodd(num):
#     print("Even")
# else:
#     print("Odd")

# obj.checkposneg(num)

# obj.checkpalindrome(num)



