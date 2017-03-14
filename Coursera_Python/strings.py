# This program is a practise program to learn strings.

# example for string concatenation
str1 = 'Hello'
str2 = 'There'

bob = str1 + " " + str2

print bob
print "\n"

str3 = '123'

res = bob + " " + str3

print res
print "\n"

# example for reading a string from user
name = raw_input("Enter a name: ")
print name
print "\n"

# example for reading a number as it is
num = input("Enter a number: ")
print num

print num + 1
print "\n"

# example for reading a number using raw_input()
num1 = raw_input("Enter a number(raw_input()): ")
print int(num1) + num
print "\n"

# string indexing and len() function

fruit = raw_input("Enter a fruit name: ")

print len(fruit)
# print fruit[1]
# print fruit[5-1]
print fruit[len(fruit)-1]
print "\n"

# looping through a string using sentinel/indefinite loop
print "looping through a string using sentinel/indefinite loop"
index = 0

while index < len(fruit):
    print index, fruit[index]
    index += 1
print "\n"

# looping through a string using for loop
print "looping through a string using for loop"

for letter in fruit:
    print letter
print "\n"

# looping and counting
print "counting the frequency of a letter"
cnt = 0
for letter in fruit:
    if letter == 'a':
        cnt += 1
print "a :", cnt
print "\n"

# string slicing
print "Slicing example"
string = "Vanilla Sunday"
print string[0:5]      # prints characters starting from 0 up-to 5(index 5 is not included)
print string[7:10]     # prints characters starting from 7 up-to 10(index 10 is not included)
print string[8:20]     # prints characters starting from 8 up-to end of the string even if the end index is off bounds
print "String length is: ", len(string)
print "\n"

# string slicing part - 2
print "Slicing example 2"
string = "Vanilla Sunday"

print string[:5]    # prints characters starting from 0 up-to 5(index 5 is not included)
print string[4:]    # prints characters starting from 7 up-to end of string
print string[:]     # prints the entire string
print "\n"

# using the 'in' operator

titan = "Annie Leonheart"
print 'n' in titan
print 'Annie' in titan
print 'mikasa' in titan

if 'Annie' in titan:
    print 'Found it!...'

# String comparision

if fruit == 'banana':
    print 'All right, bananas.'

if fruit < 'banana':
    print 'your word ' + fruit + ' comes before banana'
elif fruit > 'banana':
    print 'your word ' + fruit + ' comes after banana'
else:
    print 'All right, bananas.'

# String library functions

st = titan.lower()
print st

ut = titan.upper()
print ut

ct = titan.capitalize()
print ct

print dir(titan)    # specifies the different functions that the argument obj can call
print type(titan)   # specifies the data-type of the argument obj
pos = titan.find('Leo')     # returns the pos of the first occurrence of the sub-string(case sensitive) else returns -1
print pos

# find and replace all occurrence of the ols string with the new

rstr = titan.replace('Annie', 'Mikasa')
print rstr

rstr = titan.replace('n', 'x')
print rstr

# strip white spaces
greet = '     Hello Bob     '
print 'Left strip: ', greet.lstrip()
print 'Right strip: ', greet.rstrip()
print 'Strip(): ', greet.strip()

# string prefix's returns true or false if the string has the substring

line = 'Annie Leonheart [annieleonheart@titan.military.org]is a titan shifter and also a member of Military Police force'
print line.startswith('Annie')
print line.startswith('Loenheart')

stpos = line.find('@')      # finds the character '@' in the string
print stpos

stp = line.find(']', stpos) # finds the first occurrence of the supplied string from the specified position
domain = line[stpos + 1:stp]
print domain



