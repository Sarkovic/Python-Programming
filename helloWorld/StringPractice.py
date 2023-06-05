name = "ada lovelace"
print(name.title())
print(name.upper())
name_two = "    ADA LOVELACE    "
print(name_two.lower())

# f_strings
print(f"Hello, {name.title()}!")

# Strip method helps to remove extra whitespaces
print(name_two.strip())

name_three = "eric"
print(f"Hello {name_three.title()}, would you like to learn some Python today?")

str_quote = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
famous_person = 'Albert Einstein'
print(f"{str_quote}\n\tQuoted by, {famous_person}")

file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))