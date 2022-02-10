# 1
print([10, "ten", 10.0])

# 2
lst = [1, 1, [1,2]]
print(lst[2][1])  # 2

# 3
lst = ['a', 'b', 'c'] 
print(lst[1:])  # ["b", "c"]

# 4
week = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
print(week)

# 5
D = {"k1": [1,2,3]} 
print(D["k1"][1])  # 2

# 6
print(tuple([1,[2,3]]))  # (1, [2, 3])

# 7
set_ex = set("Mississippi")
print(set_ex)  # set(['i', 'p', 's', 'M'])

# 8
set_ex.add("X")
print(set_ex)  # set(['i', 'p', 's', 'M', 'X'])

# 9
print(set([1,1,2,3]))  # set([1, 2, 3])

# Q1
def find_num():
    result = [str(x) for x in range(2000, 3201) if (x%7 == 0) and ((x%5 != 0))]
    return " ".join(result)

print(find_num())

# Q2 
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

print(fact(int(raw_input("Enter a number for factorial: "))))

# Q3 
def dictionary(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i*i
    print(d)

dictionary(int(raw_input("Enter a number to generate a dictionary: ")))

# Q4 
def listify(num):
    list = num.split(",")
    print(list)
    print(tuple(list))

listify(raw_input("Enter a sequence of comma-separated numbers: "))

# Q5 - GIVEN
class FunString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input("Enter anything: ")

    def printString(self):
        print(self.s.upper())

strObj = FunString()
strObj.getString()
strObj.printString()
