# 1
def find_num():
    result = [str(x) for x in range(1500, 2701) if (x%7 == 0) and ((x%5 == 0))]
    return " ".join(result)

print(find_num())

# 2
def temp(degree, num):
    if degree == "c":
        print(str(num) + degree + " is " + str(int(round(((num * 9) / 5) + 32, 0))) + " in Fahrenheit")
    elif degree == "f":
        print(str(num) + degree + " is " + str(int(round(((num - 32) * 5) / 9, 0))) + " in Celsius")

temp("c", 60)
temp("f", 45)

# 3
import random

def guess_num():
    num = random.randint(1,9)
    guess = raw_input("Enter your numberical guess: ")

    while int(guess) != num:
        guess = raw_input("Enter your numberical guess: ")
    
    print("Well guessed!")

guess_num()

# 4 & 5
import math

def triangle(num):
    for i in [1, -1]:
        mid = int(math.ceil(num/2)) + 1
        if i == -1:
            start = mid
            end = 0
        else:
            start = 1
            end = mid
        for j in range(start, end, i):
            print("* " * j)

triangle(9)

# 6
def reverse_word():
    s = raw_input("Enter a word: ")
    print(s[::-1])

reverse_word()

# 7
def count(num):
    even = 0
    odd = 0

    for x in list(num):
        if x%2 == 0:
            even+=1
        else:
            odd+=1
    
    print("Number of even numbers: {} \nNumber of odd numbers: {}".format(even,odd))

count((1, 2, 3, 4, 5, 6, 7, 8, 9))

# 8
def item_type(lst):
    for x in lst:
        print(str(x) + " " + str(type(x)))

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
item_type(datalist)

# 9
for x in range(6):
    if (x == 3) or (x == 6):
        continue
    else:
        print(x)