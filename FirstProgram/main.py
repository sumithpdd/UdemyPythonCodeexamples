

def my_Function(str1, str2):
    print(str1)
    print(str2)


def print_something(name, age):
    print("My name is ",name, "my age is ",age)


def print_People(*people):
    for person in people:
        print("This person is", person)

def do_math(num1,num2):
    return  num1 + num2


my_Function("A first string","A second string")
print_something("Sumith", 40)
print_People("Nick","Dan","Jack")

math1 = do_math(5,7)
math2 = do_math(11,34)

print("First sum is", math1, "and the second one is", math2)