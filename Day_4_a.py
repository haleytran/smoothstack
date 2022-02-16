# 1
from re import M


def func():
    print("Hello World")

func()  # Hello World

# 2
def func1(name):
    print("Hi My name is Google")

func1("John")  # Hi My name is Google

# 3
def func3(x, y, z):
    return (x if z == True else y)

print(func3("hello", "goodbye", False))  # goodbye

# 4
def func4(x, y):
    return x*y

print(func4(3,4))  # 12

# 5
def is_even(num):
    return (True if num%2 == 0 else False)

print(is_even(4))  # True
print(is_even(5))  # False

# 6
def greater(x, y):
    return (True if x > y else False)

print(greater(5,6))  # False
print(greater(6,5))  # True

# 7
def add(*args):
    return sum(args)

print(add(1,2))  # 3
print(add(1,2,3,4))  # 10

# 8
def list_even(*args):
    return [x for x in args if x%2 == 0]

print(list_even(1,2,3))  # [2]

# 9 
def silly_string(s):
    return "".join([s[i].upper() if i%2 != 0 else s[i].lower() for i in range(len(s))])

print(silly_string("word"))  # wOrD

# 10
def magic_num(num1, num2):
    if num1%2 == 0 == num2%2:
        return (num1 if num1 < num2 else num2)
    else:
        return (num1 if num1 > num2 else num2)

print(magic_num(1,1))  # 1
print(magic_num(3,5))  # 5
print(magic_num(1,2))  # 2
print(magic_num(2,2))  # 2
print(magic_num(4,2))  # 2

# 11
def is_same_first_letter(s1, s2):
    return (True if s1[0].lower() == s2[0].lower() else False)

print(is_same_first_letter("string", "same"))  # True
print(is_same_first_letter("string", "different"))  # False

# 12
def twice_as_far(num):
    return (7+(2*(7-num)) if num < 7 else 7-2*(num-7))

print(twice_as_far(5))  # 11
print(twice_as_far(9))  # 3

# 13
def strange_string(s):
    return "".join([s[i].upper() if i == 0 or i == 3 else s[i] for i in range(len(s))])

print(strange_string("string"))  # StrIng