# Write a function that accepts two arguments (length, start) to generate an array of a specific length 
# filled with integer numbers increased by onefrom start.

def increaseFromStart(start, length):
    arr=[]
    for i in range(length):
        arr.append(start)
        start+=1
    return arr
print(increaseFromStart(2,8))


#write a function that takes a number as an argument and if the numberdivisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and 
# if is isdivisible by both return "FizzBuzz"

def visble(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz") 
    
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print("Not divible by 3 and 5")
visble(60)



# Write a function which has an input of a string from user then it will return the same string reversed.

def takeStr(inp):
    return inp[::-1]


takeStr("Youssef")



# Ask the user for his name then confirm that he has entered  his name(not an empty string/integers). then proceed 
#  to ask him for his email andprint all this data(Bonus) check if it is a valid email or not

import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def info (name):
    # isinstance
    if type(name) == str:
        while True:
            email =  input("Enter Your Email Address : ")
            if re.fullmatch(regex, email):
                print(f"Your Name is {name} and your Email Address is {email}")
                break
    else:
        print("Name must be string") 

info("youssef")

# info(12)




# abdulrahman
name = 'ahmed'
c = name[0]
longTerm = ''


for charName in range(1,len(name)):
     if ord(c) < ord(name[charName]):
         longTerm+=c
         c = name[charName]
            
longTerm+=c
          
print(longTerm)


arr =[]
sum = 0
while True:
    num = input("Enter Numbers : ")
    if not num.isnumeric():
        if num == "done":
            break
        num = input("Enter Only numbers : ")

    elif num.isnumeric():
        arr.append(num)
    else:
        num = input("Do you want to enter another number : ")
# print(type(arr[1]))
for num in arr:
    sum+=int(num)
length = len(arr)
print(f"sum => {sum}")
print(f"Length => {length}")
print(f"The Average is =>{sum/length}")




# Q7 hangman
import random

lst =['youssef','amr','david','kareem','alaa']

def gussFun():
    guess = input("Enter Your Guess : ")
    if random.choice(lst) == guess:
        print(random.choice(lst),guess)
        print(guess,"is correct Congratulations!")
    else:
        # print(guess,"is incorrect Try Again!")
        guess = input("Enter Your Guess : ")

gussFun()    




import random
words=['youssef','alaa','kareem']
word=random.choice(words)
turns=7
name=input("Enter your name please: ")

print(f"Hello {name} start the play")

print("Guess the characters")
guesses = ''

while turns > 0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char)
		else:
			print("_")
			failed += 1

	if failed == 0:
		print("You Win")
		print("The word is: ", word)
		break

	guess = input("guess a character:")

	guesses += guess
	if guess not in word:

		turns -= 1
		print("Wrong")
		print(f"You have {turns} more guesses")

		if turns == 0:
			print("You Loose")