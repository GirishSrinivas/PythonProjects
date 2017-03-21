# TEXT = "a href=\"http://www.wrong.org\"<a href=\"correct\">Example2 a href /a</a> URL"
TEXT = "<a href=\"http://www.example.org\">Example1</a>"
print "Length of TEXT: ", len(TEXT)
print TEXT
pos = TEXT.find("<a href=\"") + 9
print pos
pos2 = TEXT.find("\">", pos)
print pos2
email = TEXT[pos:pos2]
print email

