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


# str_len_no_lib_func()
# str_concat_no_lib_func()
