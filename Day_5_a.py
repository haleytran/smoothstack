def BMI(weight, height):
    return weight/height**2

def grade(lst):
    if len(lst) == 0:
        return ""

    weight, height = lst.pop(0).split()
    val = BMI(float(weight), float(height))

    if val >= 30.0:
        result = "obese"
    elif val >= 25.0:
        result = "over"
    elif val >= 18.5:
        result = "normal"
    else:
        result = "under"

    return "{} ".format(result) + grade(lst)

def classify_BMI():
    num = input("Enter how many people: ")
    data = [input("Enter weight(kg) followed by height(m), space-separated: ") for i in range(int(num))]

    return grade(data)

print(classify_BMI())