# 1
print("Hello World"[8])  # r

# 2
print("thinker"[2:5])  # ink
S = "hello"
print(S[1])  # e

# 3
S = "Sammy"
print(S[2:])  # mmy

# 4
print(set("Mississippi"))  

# 5
def palindrome(num, lst):
    if len(lst) > 0:
        phrase = lst[0].lower().replace(" ","")  # Makes string all lowercase and removes spaces
    else:
        return ""
    
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''  # Removes any special characters
    for char in punc:
        phrase = phrase.replace(char, "")
    
    if phrase == phrase[::-1]:  # Determines if the phrase is a palindrome
        result = "Y" 
    else:
        result = "N"

    return result + " " + palindrome(num, lst[1:])  # Concatenates the result of each phrase, separated by a space

print(palindrome(3,["Stars","O, a kak Uwakov lil vo kawu kakao!","Some men interpret nine memos"]))