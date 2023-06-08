# 1. Program to find the length of the string without
# any library function
def str_len_no_lib_func():
    input_string = input()
    cnt = 0
    for _ in input_string:
        cnt += 1
    print(cnt)


# 2. Program to concatenate two string w/o any library functions
def str_concat_no_lib_func():
    input_str_one = input()
    input_str_two = input()

    print(f"{input_str_one}{input_str_two}")


# 3. Program to count the vowels
def str_count_vowels():
    input_string = input()
    # Initialize a list of all the vowels, capital letter and small letter
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    # Initialize a counter
    vowel_count = 0
    for char in input_string:
        # Check if the current selected character is in the list of vowels
        # If found increment the vowel counter
        if vowels.__contains__(char):
            vowel_count += 1
    print(vowel_count)


# 4. Program to count the number of words
def str_count_words():
    input_string = input()
    # If the string is empty the answer will be 0
    if len(input_string) == 0:
        return 0
    # Initialize with 1 to include the first word
    words_count = 1
    for char in input_string:
        # Check if the current character is a whitespace/tab/newline,
        # if yes then increment the space counter
        if char == " " or char == "\t" or char == "\n":
            words_count += 1
    # The number of words will be number of spaces + 1
    return words_count


# str_len_no_lib_func()
# str_concat_no_lib_func()
# str_count_vowels()
print(str_count_words())