"""
name = input('Please Enter your name')
color = input('Please Enter your fav color')
print(name + ' likes ' + color)
"""
"""
revString = 'hello how are you'
length = len(revString)
for i in revString[17::-1]:
    print(i, end='')
else:
    print()
"""
"""
txt = "Hello World" [::-1]
print(txt)
"""
"""
course = "hello this is my course"
print(len(course))
U_course = course.upper()
print(U_course)
E_course = course.encode(encoding='ascii', errors='strict')
print(E_course)
"""
'''
revString = 'hello how are you'
replaceStr = revString.replace('hello', 'hi')
print(replaceStr)
'''
'''
revString = 'hello how are you'
T_revString = revString.title()
print(T_revString)
'''

'''
PriceHouse = 1000000
GoodCredit = 200
BuyerCredit = input("Please enter credit of the buyer")
if int(BuyerCredit) >= GoodCredit:
    price = PriceHouse - PriceHouse * .1
    print("10% less " + str(price))
else:
    price = PriceHouse - PriceHouse * .2
    print("20% less " + str(price))
print(f"Down Payment must be {price}")
'''
'''
name = input("Enter Your name")
if len(name) <= 3:
    print("Name must be at least more than three character")
elif len(name) >= 8:
    print("Name must be less than 8 character")
else:
    print("Name looks good")
'''
'''
Weight = input("Enter you weight")
Unit = input("(L)bs or (K)g")

if Unit.casefold() == "l":
    Weight = int(Weight) / 2.205
    print("You Are " + str(Weight) + " Kilos")
elif Unit.casefold() == "k":
    Weight = int(Weight) * 2.205
    print("You Are " + str(Weight) + " Pound")
else:
    print("Please enter correct Unit")
'''

'''
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
j = 4
while j < 5 | j >= 1:
    print("*" * j)
    j = j - 1
'''
'''
command = ""
flagStart = False
while True:
    User_Input = input("> ").upper()
    if User_Input == "START":
        if flagStart:
            print("Car is already started")
        else:
            flagStart = True
            print("Car Started... Ready to go")
    elif User_Input == "STOP":
        if not flagStart:
            print("Car is already stopped")
        else:
            flagStart = False
            print("Car Stopped")
    elif User_Input == "HELP":
        print("""
start = to start the car
stop = to stop the car
quit = to exit
            """)
    elif User_Input == "QUIT":
        print("BYE")
        break
    else:
        print("I don't understand that")
'''
'''
prices = [10, 20, 30]
total = 0
for cost in prices:
    total = cost + total
print(f"total: {total}")
'''
"""
number = [5, 2, 5, 2, 2]
for i in number:
    print("*" * i)
"""
"""
number = [5, 1, 9, 34]
maxi = number[0]
for i in number:
    if i > maxi:
        maxi = i
print(maxi)
"""

'''
Sentence = input("Enter Your Sentence")
words = Sentence.split(" ")
print(words)
for i in words:
    if len(i) % 2:
    hh = i[::-1]
    print(hh, end=' ')
'''
'''
Sentence = input("sentence")
words = Sentence.split(" ")
for i in words:
    print(len(i))
    rev = i[::-1]
    sents = print(rev, end=" ")
'''
'''
numbers = [1, 3, 6, 9, 10]
numbers.sort()
numbers.reverse()
print(numbers)
'''
"""
numbers = [1, 1, 1, 9, 3, 6, 1, 9, 10, 10]
numbers2 = numbers.copy()
for i in numbers:
    numbers.remove(i)
    if i in numbers:
        continue
    else:
        numbers.insert(len(numbers), i)
print(numbers)
"""
"""
number = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}
userInput = list(input("Phone Number"))
for i in userInput:
    print(number[i], end=" ")
"""
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "smile",
    ":(": "sad"
}
output = ""
for i in words:
    output += emojis.get(i, i) + " "
print(output)
