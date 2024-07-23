# strings are immutable
a="easy||||||||||"
print(len(a))
print(a.upper())
print(a.lower())
# following element are used for cut the only last word which we want to cut.
print(a.rstrip("|")) 
print(a.replace("easy", "john"))
#fallowing element is used to split words into a list.
b="easy||||s  ||| |||"
print(b.split(" "))


