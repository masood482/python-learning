j = [1, ' this is what we {0}ly get for disobeying the {1}, who created us ', 9.2, True, 1j,['one',1],('two',2),{'name':'mas482','dob':4},range(100)]
a,b,c,d,e,f,g,h,i = j
print(a) #int

print(b)#str
print(b[8])#str indexing
print(len(b))# length
print('get' in b)# true if exists else false
print('when' not in b)#false if exists else true
print(b.upper())#uppercase
print(b.lower())#lowercase
print(b.strip())#remove whitespace
print(b.replace('at','en'))#replace text
print(b.split(','))#list broken by ','
print(b.format(d,a))#template literal of python- fills the {} inside the string b with a
print("\rthey said,\f'we will  \bnot believe'"+'\fand \nhence they became the people of the \'fire\'')#carriage return,form feed,back space,concat,new line,escape
'''
capitalize()#	Converts the first character to upper case
casefold()#	Converts string into lower case
center()#	Returns a centered string
count()#	Returns the number of times a specified value occurs in a string
encode()#	Returns an encoded version of the string
endswith()#	Returns true if the string ends with the specified value
expandtabs()#	Sets the tab size of the string
find()#	Searches the string for a specified value and returns the position of where it was found
format()#	Formats specified values in a string
format_map()#	Formats specified values in a string
index()#	Searches the string for a specified value and returns the position of where it was found
isalnum()#	Returns True if all characters in the string are alphanumeric
isalpha()#	Returns True if all characters in the string are in the alphabet
isdecimal()#	Returns True if all characters in the string are decimals
isdigit()#	Returns True if all characters in the string are digits
isidentifier()#	Returns True if the string is an identifier
islower()#	Returns True if all characters in the string are lower case
isnumeric()#	Returns True if all characters in the string are numeric
isprintable()#	Returns True if all characters in the string are printable
isspace()#	Returns True if all characters in the string are whitespaces
istitle()#	Returns True if the string follows the rules of a title
isupper()#	Returns True if all characters in the string are upper case
join()#	Joins the elements of an iterable to the end of the string
ljust()#	Returns a left justified version of the string
lower()#	Converts a string into lower case
lstrip()#	Returns a left trim version of the string
maketrans()#	Returns a translation table to be used in translations
partition()#	Returns a tuple where the string is parted into three parts
replace()#	Returns a string where a specified value is replaced with a specified value
rfind()#	Searches the string for a specified value and returns the last position of where it was found
rindex()#	Searches the string for a specified value and returns the last position of where it was found
rjust()#	Returns a right justified version of the string
rpartition()#	Returns a tuple where the string is parted into three parts
rsplit()#	Splits the string at the specified separator, and returns a list
rstrip()#	Returns a right trim version of the string
split()#	Splits the string at the specified separator, and returns a list
splitlines()#	Splits the string at line breaks and returns a list
startswith()#	Returns true if the string starts with the specified value
strip()#	Returns a trimmed version of the string
swapcase()#	Swaps cases, lower case becomes upper case and vice versa
title()#	Converts the first character of each word to upper case
translate()#	Returns a translated string
upper()#	Converts a string into upper case
zfill()# fills the string;
'''

print(b.swapcase()[5:10])

print(c)#float
print(a+c,a-c,a*c,a/c,a%c,a**c,a//c)#arithmetic operators
print(a is c)#identity operator is
print(a is not c)#identity operators is not
print(a in f)#membership operators in
print(c not in f)#membership  operators not in


print(d)#boolean
print(bool(""),bool(None),bool(0),bool([]),bool({}),bool(()),bool(False))#all are falsy
print(bool('1'),bool(1),bool([1]),bool({'one':1}),bool((1)),bool(True))#all are truthy
print(isinstance(c,float))# function, which can be used to determine if an object is of a certain data type:

print(e)#complex
print(f)#list
print(g)#tuple
print(h)#dict
print(i)#range

print(j)#list
print(len(j))#length
print(j[1],j[-7])#index 1
print(j[1:4],j[-8:-5])#returns array of second,third and fourth element
j[1] = 'no one has the right to be worshipped but he' #add new element
print(j)#listprint(j)#listprint(j)#list

print(type(a),type(b))
 
if 'is' in j:
 print('yes')
else :
 print('no')
for x in j:
 print(x)

[print(x) for x in f]
k = [x.upper() for x in j if "is" in str(x)]
print(k)
l = [x+'two' if x=='i' else x+'one' for x in j if 'i' in str(x)]
m = list(j)
m.append('we')
print(m)
p = j[1].split()
print(p)
q = p.extend(m)
print(q)


