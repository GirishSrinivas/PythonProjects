"""
Sample stRING script
"""
# This program is a practise program to learn stRINGs.
# example for stRING concatenation
STR1 = 'Hello'
STR2 = 'There'

BOB = STR1 + " " + STR2

print(BOB)

STR3 = '123'

RES = BOB + " " + STR3

print(RES)

# example for reading a stRING from user
NAME = raw_input("Enter a NAME: ")
print(NAME)

# example for reading a number as it is
NUM = input("Enter a number: ")
print(NUM)

print(NUM + 1)

# example for reading a number using raw_input()
NUM1 = raw_input("Enter a number(raw_input()): ")
print(int(NUM1) + NUM)


# stRING INDEXing and len() function

FRUIT = raw_input("Enter a FRUIT NAME: ")

print(len(FRUIT))
# print(FRUIT[1]
# print(FRUIT[5-1]
print(FRUIT[len(FRUIT)-1])

# looping through a stRING using sentinel/indefinite loop
print("looping through a stRING using sentinel/indefinite loop")
INDEX = 0

while INDEX < len(FRUIT):
    print(INDEX, FRUIT[INDEX])
    INDEX += 1
print("\n")

# looping through a stRING using for loop
print("looping through a stRING using for loop")

for letter in FRUIT:
    print(letter)

# looping and counting
print("counting the frequency of a letter")
CNT = 0
for letter in FRUIT:
    if letter == 'a':
        CNT += 1
print("a :", CNT)

# stRING slicing
print("Slicing example")
STRING = "Vanilla Sunday"
print(STRING[0:5])     # prints characters starting from 0 up-to 5(INDEX 5 is not included)
print(STRING[7:10])    # prints characters starting from 7 up-to 10(INDEX 10 is not included)
print(STRING[8:20])   # prints string from 8 up-to end of the string even if it is off bounds
print("stRING length is: ", len(STRING))

# stRING slicing part - 2
print("Slicing example 2")
STRING = "Vanilla Sunday"

print(STRING[:5])   # prints characters starting from 0 up-to 5(INDEX 5 is not included)
print(STRING[4:])    # prints characters starting from 7 up-to end of stRING
print(STRING[:])     # prints the entire stRING

# using the 'in' operator

TITAN = "Annie Leonheart"
print('n' in TITAN)
print('Annie' in TITAN)
print('mikasa' in TITAN)

if 'Annie' in TITAN:
    print('Found it!...')

# stRING comparision

if FRUIT == 'banana':
    print('All right, bananas.')

if FRUIT < 'banana':
    print('your word ' + FRUIT + ' comes before banana')
elif FRUIT > 'banana':
    print('your word ' + FRUIT + ' comes after banana')
else:
    print('All right, bananas.')

# stRING library functions

ST = TITAN.lower()
print(ST)

UT = TITAN.upper()
print(UT)

CT = TITAN.capitalize()
print(CT)

print(dir(TITAN))    # specifies the different functions that the argument obj can call
print(type(TITAN))   # specifies the data-type of the argument obj
POS = TITAN.find('Leo')  # returns the POS of the first occurrence of the sub-string else returns -1
print(POS)

# find and replace all occurrence of the ols stRING with the new

RSTR = TITAN.replace('Annie', 'Mikasa')
print(RSTR)

RSTR = TITAN.replace('n', 'x')
print(RSTR)

# strip white spaces
GREET = '     Hello BOB     '
print('Left strip: ', GREET.lstrip())
print('Right strip: ', GREET.rstrip())
print('strip(): ', GREET.strip())

# string prefix's returns true or false if the string has the substring

LINE = 'Annie Leonheart [annieleonheart@TITAN.military.org]' \
       'is a TITAN shifter and also a member of Military Police force'
print(LINE.startswith('Annie'))
print(LINE.startswith('Loenheart'))

STPOS = LINE.find('@')      # finds the character '@' in the string
print(STPOS)

STP = LINE.find(']', STPOS)  # finds the first occurrence of the stRING from the given position
DOMAIN = LINE[STPOS + 1:STP]
print(DOMAIN)
