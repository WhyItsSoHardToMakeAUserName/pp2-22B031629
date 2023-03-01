import re

text = open("row.txt")
txt_file = text.read()

x = re.split("\s",txt_file)


# #Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

for i in x:
    result = re.search("a(b)*",i)
    if result:
      print(result.string)

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
for i in x:
    result = re.search("a(b){2,3}",i)
    if result:
      print(result.string)

# Write a Python program to find sequences of lowercase letters joined with a underscore.
for i in x:
    result = re.search("[a-z](_[a-z])+",i)
    if result:
      print(result.string)

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
for i in x:
    result = re.search("[a-z](_[a-z])+",i)
    if result:
      print(result.string)

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
for i in x:
    result = re.search("a.*b",i)
    if result:
      print(result.string)

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
for i in x:
    result = re.sub("\s",":",i)
    result = re.sub("_",":",i)
    result = re.sub(",",":",i)

# Write a python program to convert snake case string to camel case string.
for i in x:
    string=""
    if re.search("_",i):
        split= re.split("_",i)
        string+=split[0].lower()
        for i in range(1,len(split)):
            string+=split[i].capitalize()
        print(string)

# Write a Python program to split a string at uppercase letters.
x = re.split("[A-Z]",txt_file)
print(x)

# # Write a Python program to insert spaces between words starting with capital letters.
for i in x:
    spaced_string = re.sub('([A-Z][a-z]*)', r' \1', i)
    print(spaced_string)
# Write a Python program to convert a given camel case string to snake case.
for i in x:
    string=""
    if re.search("_",i):
        split= re.split("_",i)
        string+=split[0].lower()
        for i in range(1,len(split)):
            string=string+"_"+split[i].lower()
        print(string)