varsity_name = 'UIU'

def say_hi(name, greeting):
    # global varsity_name
    varsity_name = 'BUET'
    print(f"{greeting} {name} from {varsity_name}")

say_hi(greeting='Hola', name='John')
print(varsity_name)