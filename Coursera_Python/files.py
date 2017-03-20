# Files I/O
# how to open a file

fp = open('text.txt', 'r')
print fp

# Reading a file with extra new line...
count = 0
print 'the content of the file is:'
for line in fp:
    print line
    count += 1
fp.close()
print 'Number of lines in the file is: ', count

# how to read the entire file in one shot
# use this method of reading only for small files
fp = open('text.txt', 'r')
print 'Using the read()'
text = fp.read()
print len(text)
print text[:4]
print text
fp.close()

fp = open('text.txt')
for line in fp:
    if line.startswith('From'):
        print line
fp.close()

fp = open('text.txt')
for line in fp:
    line = line.strip().upper()
    print line
fp.close()


