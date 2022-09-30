'''

j = [1, ' this is what we {0}ly get for disobeying the {1}, who created us ', 9.2, True, 1j,['one',1],('two',2),{'name':'mas482','dob':4},range(100)]
a,b,c,d,e,f,g,h,i = j
print("1. ",a) #int

print("2. ",b)#str
print("3. ",b[8])#str indexing
print("4. ",len(b))# length
print("5. ",'get' in b)# true if exists else false
print("6. ",'when' not in b)#false if exists else true
print("7. ",b.upper())#uppercase
print("8. ",b.lower())#lowercase
print("9. ",b.strip())#remove whitespace
print("10. ",b.replace('at','en'))#replace text
print("11. ",b.split(','))#list broken by ','
print("12. ",b.format(d,a))#template literal of python- fills the {} inside the string b with a
print("13. ","\rthey said,\f'we will  \bnot believe'"+'\fand \nhence they became the people of the \'fire\'')#carriage return,form feed,back space,concat,new line,escape

'''

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

'''

print("14. ",b.swapcase()[5:10])

print("15. ",c)#float
print("16. ",a+c,a-c,a*c,a/c,a%c,a**c,a//c)#arithmetic operators
print("17. ",a is c)#identity operator is
print("18. ",a is not c)#identity operators is not
print("19. ",a in f)#membership operators in
print("20. ",c not in f)#membership  operators not in


print("21. ",d)#boolean
print("22. ",bool(""),bool(None),bool(0),bool([]),bool({}),bool(()),bool(False))#all are falsy
print("23. ",bool('1'),bool(1),bool([1]),bool({'one':1}),bool((1)),bool(True))#all are truthy
print("24. ",isinstance(c,float))# function, which can be used to determine if an object is of a certain data type:

print("25. ",e)#complex
print("26. ",f)#list

print("27. ",g)#tuple

print("28. ",h)#dict
print("29. ",i)#range


#list

print("30. ",j)#list
print("31. ",len(j))#length
print("32. ",j[1],j[-7])#index 1
print("33. ",j[1:4],j[-8:-5])#returns array of second,third and fourth element

j[1] = 'no one has the right to be worshipped but he' #add new element
print("34. ",j)#list

j.insert(0,'three')#inserts the element between 0 and 1 index
print("35. ",j)#list

j.append('are')#adds element at the end like push() in js
print("36. ",j)#list

j.extend(f)#appends an array f to array j
print("37. ",j)#list

j.remove('are')#removes the element 'are' from array j
print("38. ",j)#list

j.pop(1)#removes the element 1 from array j if empty removes the last
print("39. ",j)#list

del j[2]#removes the third element if no index given removes the array
print("40. ",j)#list

j.clear()#empties the array leaving only [] behind
print("41. ",j)#list
#creating a list using list() we use round brackets () rather than square []
j = list((1, ' this is what we get for that ', 9.2, True, 1j))
print("42. ",j)#list

for x in j: #for loop for printing all the elements in a new line must end with colon :
 print("41(under For Loop). ",x)#indentation of at least one space required for content of loop
 print("(inside the for loop) ")#inside the loop
print("42. (outside the for loop)")#outside the loop

for i in range(len(j)):
 print("43. (inside the for loop)",j[i])#inside the loop

i=0
while i < len(j):#while loop for printing all the elements must end with colon :
 print("44. (inside the while loop)",j[i])#inside the loop
 i = i + 1 # still inside the loop and incrementing the value of i
print("45. (outside the while loop)")#outside the loop

newList = []#empty array
for x in j:#for loop
 if "wh" in str(x):# if statement inside the for loop and converting current element to string
  newList.append(x)# adding the element to newList if condition true
print("46. ",newList)#list

newList = [x for x in j if 'wh' in str(x)]# the above 4 lines can be compressed by list comprehension
#it can be read as 'add element x in list newList 
# for the element x in list j if string 'wh' is present 
# in the current element x
print("47. ",newList)#list

newList = [x for x in range(10) if x%2==0]# create a list with elements from range 0 to 10
# where the element must be perfectly divisible by 2 
print("48. ",newList)#list

newList = [x for x in j if type(x)!=int]# create a list of x elements from j 
#if data type of current element x is not integer 
print("49. ",newList)#list

newList = [x if type(x)==complex else 'not present' for x in j]# create a list 
# from j where if the current element is complex copy from j 
# else return string 'not present
print("50. ",newList)#list

k = ['one','two','three','four']
l = [1,3,4,2]
k.sort()# sort ascending
l.sort()# sort ascending
print("51. ",k,l)#list

k.sort(reverse=True)# sort descending
print("52. ",k,l)#list

def sortFunc(n):# function definition
 return abs(n-1)# return it

l.sort(key = sortFunc)# use the function to sort by setting Keys i.e. 
# elements inside the list to the returned value  
print("53. ",l)#list

k.sort(key = str.lower)# case-insensitive sort
print("54. ",k)#list

k.reverse()# reverses the string
print("55. ",k,l)#list

m  = j # here m is just a reference of j, any change in j will reflect on m
m = j.copy()# this will copy the value of list j in list m 
print("56. ",m)#list

m = list(j)#this is also a method of copying the list
print("57. ",m)#list

n = k+l # adding two list
print("58. ",n)#list

l = [x for x in k]# all elements of k are added in l
print("59. ",l)#list

l.extend(k)#add k at the end of l 
print("60. ",l)#list

'''

'''
append()#	Adds an element at the end of the list
clear()#	Removes all the elements from the list
copy()#	Returns a copy of the list
count()#	Returns the number of elements with the specified value
extend()#	Add the elements of a list (or any iterable), to the end of the current list
index()#	Returns the index of the first element with the specified value
insert()#	Adds an element at the specified position
pop()#	Removes the element at the specified position
remove()#	Removes the item with the specified value
reverse()#	Reverses the order of the list
sort()#	Sorts the list
'''

'''

#tuple

p = ('one')#string
print("61. ",type(p))#string
p = ('one',)#tuple need two items separated by ,
print("62. ",type(p))#tuples have everything same as list except no changes 
#can be made once created.they can have duplicates  

p = ('one','two','three','four')#tuple
print("63. ",p)#tuple
q = list(p)#convert tuple to list
q.append('five')# make changes to list
p = tuple(q)# convert the list back to tuple
print("64. ",p)#tuple

q = ('six',)# new tuple
p = p + q # adding two tuples
print("65. ",p)# tuples

del q #delete the tuple
# tuples q does not exist now

(one,two,*three_five,six) = p #unpacking the tuple to assign
# variables one='one',two='two',six='six' and assigning string
# 'three','four' and 'five' to list three_five by adding the * in front
print("66. ",p,'\n',one,two,three_five,six)# tuples

#looping tuple is similar to list
# for loop
# for in loop
# for in using range() and len()
# # while loop 

q = p+p #tuple added together
print("66. ",q)# tuples 
q = p*2 #tuple multiplies
print("67. ",q)# tuples

'''
'''

count()#	Returns the number of times a specified value occurs in a tuple
index()#	Searches the tuple for a specified value and returns the position of where it was found
'''

'''

# set

s = {'one','two','three','four','three'}# unordered, unchangeable, and unindexed
# duplicates not allowed
# Once a set is created, you cannot change its items, but you can remove 
# items and add new items
print("68. ",s)# set
# using set((value)) new set can be created
# type is <class 'set'>
# len() gives the length
# to get value of the set use for in loop
# get boolean true or false by using 'value' in set
# clear() empties the set
# del deletes the set

s.add('five')# add element to set
print("69. ",s)# set

r = {'six','seven'}
s.update(r)# add the set r to set s
# update can be used for adding set to set ,list to set or tuple to set
print("70. ",s)# set

s.remove('six')# remove element make sure the element exists
print("71. ",s)# set

s.discard('seven')# remove element
print("72. ",s)# set

t = s.pop()# removes the last element but set are unordered so you dont know 
# what got removed
# pop() stores the value that it removed
print("73. ",s)# set
print("74. ",t)# set

s.union(r)# join sets
print("75. ",s)# set

s.intersection_update(r)# gives the duplicates between the two sets
print("76. ",s)# set

s.symmetric_difference_update(r)# gives the non duplicates
print("77. ",s)# set

'''

'''
add()#	Adds an element to the set
clear()#	Removes all the elements from the set
copy()#	Returns a copy of the set
difference()#	Returns a set containing the difference between two or more sets
difference_update()#	Removes the items in this set that are also included in another, specified set
discard()#	Remove the specified item
intersection()#	Returns a set, that is the intersection of two other sets
intersection_update()#	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()#	Returns whether two sets have a intersection or not
issubset()#	Returns whether another set contains this set or not
issuperset()#	Returns whether this set contains another set or not
pop()#	Removes an element from the set
remove()#	Removes the specified element
symmetric_difference()#	Returns a set with the symmetric differences of two sets
symmetric_difference_update()#	inserts the symmetric differences from this set and another
union()#	Return a set containing the union of sets
update()#	Update the set with the union of this set and others


'''
'''

# Dictionary

t = {'name':'one','add':2,'cont':['three','four'],'male':True}# Dictionary items are ordered, 
# changeable, and does not allow duplicates.duplicates will overwrite the existing value
# Dictionary items are presented in key:value pairs,
#  and can be referred to by using the key name.
print("78. ",t)# dict
print("79. ",t['cont'])# get value using key 
print("80. ",t.get('cont'))# get value using get()

# using dict((value)) new set can be created
# type is <class 'dict'>
# len() gives the length
# to get all keys of the dict use for in loop
# get boolean true or false by using 'value' in dict
# clear() empties the dict
# del deletes the dict

u = t.keys()# gives out the keys of dict t in the form of list inside dict_keys()
print("81. ",u)# dict_keys()

t['edu'] = 'grad'
print("82. ",u)# dict

u = t.values()# gives out the values of dict t in the form of list inside dict_values()
print("83. ",u)# dict

u = t.items()# gives each item in dict as tuples in a list
print("84. ",u)# dict

if 'edu' in t: # checks if key 'edu' exists in dict t
 print("85. ",'edu:'+t['edu'])# dict
else:
 None

t.update({'char':'good'})# adds key value pair to an 
# existing dict or 

t.update({'name':'two'})# changes the existing values 
print("86. ",t)# dict

for x in t:
 print("87. ",x)# Print all key names

for x in t:
 print("88. ",t[x])# Print all value names

for x in t.values():# using values() to print values 
 print("89. ",x)# Print all values names

for x in t.keys():# using keys() to print all the keys
 print("90. ",x)# Print all key names

for x,y in t.items():# using the items() to print all the key-value pair 
 print("91. ",x,y)# Print all key-value names

u = t.copy()# copy using copy()
u = dict(t)# copy using the constructor
print("92. ",u)# Print all key names 

v = {'tee':t,'you':u}# nested dict
print("93. ",v)# Print all key names

t.pop('char')# removes the key 'char' and its associated value
t.popitem()# removes the last key-value pair
del t['add'] # removes the 'add' key and its value 
print("94. ",t)# dict

'''

'''
clear()#	Removes all the elements from the dictionary
copy()#	Returns a copy of the dictionary
fromkeys()#	Returns a dictionary with the specified keys and value
get()#	Returns the value of the specified key
items()#	Returns a list containing a tuple for each key value pair
keys()#	Returns a list containing the dictionary's keys
pop()#	Removes the element with the specified key
popitem()#	Removes the last inserted key-value pair
setdefault()#	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()#	Updates the dictionary with the specified key-value pairs
values()#	Returns a list of all the values in the dictionary
'''

'''

# if elif else
w = True
if w :# if statement
 print("95. ",w)#
elif "":# else if
 print("96. ",~w)# Print
else :# else
 print("97. ",None)# Print

# shorthand if else 
if w:print("96. ",'no')# shorthand if

print("97. ","yes") if w else print("98. ","no")# shorthand if else

print("98. ",'yes') if w else print("99. ",'no') if "" else print("100. ",'maybe')# Ternary Operators, 
#or Conditional Expressions.

if w and d:
 print("100. ",w,d)

if w or d:
 print("101. ",w,d)


'''

if 1 < 2:
 pass #placeholder for an empty if statement 


# while loop

i = 0
while i < 3:
 print('102. ',i)#
 i += 1# inside the while loop
 if i == 2:# inside the while loop
  break# inside the if statement inside the while loop 
  #break stops the loop 


i = 0
while i < 4:
 print('103. ',i)#
 i += 1# inside the while loop
 if i == 2:# inside the while loop
  continue# inside the if statement inside the while loop 
  #continue stops the current loop and jumps to the next


i = 0
while i < 5:
 print('104. ',i)#
 i += 1# inside the while loop
else:# comes in to effect only once after the loop ends
 print('105. ','loop end')

# for loop

for x in "welcome":# loop through string
 if x == 'c':
  break;# stops when 'c' reached
 print('106. ',x)# 

for x in "welcome":# loop through string
 if x == 'c':
  continue;# skips when 'c' reached
 print('107. ',x)# 


for x in ['one',1]:# loop through list
 print('108. ',x)# 

for x in ('one',1):# loop through tuple
 print('109. ',x)# 

for x in {'one',1}:# loop through set
 print('110. ',x)# 

for x in {'one':1}:# loop through dict
 print('111. ',x)#

for x in range(3,10,2):# loop through range
  #first para is start
  #second para is the end
  #third para is the increment
 print('112. ',x)# 

for x in range (4):
 if x == 2:
  break# breaks after reaching 2
 print('113. ',x)#
else:# else statement not executed because loop broke
 print('114. ','completed')#


for x in ['one',1]:
 for y in ['two',2]:#for every loop of x, y loops len() times of array
  print('115. ',x,y)#
 
for x in [1,2]:
 pass # placeholder for the empty for loop

# functions

def func1(x,y): # functions start with key word def
  # name of the function needs to end with parenthesis ()
  # followed by colons :
  print(x,'\b. ','did you '+ y +'?')# function body
 
func1(116,'call') # call of the function needs the name and parenthesis 
func1(117,'know')
func1(118,'understand the function call')# the value inside the paranthesis 
# is called argument .the argument is passed to the parameter inside 
# the function which gets used inside the function body
# the no of arg and para need to be equal or else you get an error

def func2(*y): # if the no of args are unknown put a *
  for x in y: # the no of args are stored in a tuple y
   print('119. ',x)# the items are printed using the for loop

func2(1,2,3,4,5,6,7,8)

def func2(y): # passing a list as an argument
  for x in y:
    print('123. ',x)

y = [1,2,3,4,5,6,7,8]
func2(y)

def func3(o,a,b,ab):
  print('120. ','your blood group is',o)#

func3(o = 'O+',a = 'A+',b = 'B+',ab = 'AB+')# passing key-value as
# arguments in this the order of the args and the para are not important
# also known as kwargs

def func4(**blood):# if the no of kwargs are unknown put two * before
  print('121. ','your blood group is',blood['ab'])## the no of 
  # kwargs are stored in a dict blood

func4(o = 'O+',a = 'A+',b = 'B+',ab = 'AB+')#

def func5(blood = 'not yet known'): # default para is used in case the args are not 
  # passed
  print('122. ','your blood group is',blood)#

func5()# empty call
func5('A+')

# simple calculator using function and return

def func6(x,y,z):
  
  if y == '+': 
    return x+z
  elif y == '-':
    return x-z
  elif y == '*':
    if x == 0 and z == 0:
      return 'infinity'
    else:
      return x*z
  elif y == '/':
    if z == 0:
      return 'infinity'
    else:
      return x/z
  else :  
      return 'expression needs to be one of these: +,-,*,/'
  

print('124. ',func6(2,'+',-3))# 
print('125. ',func6(2,'-',-3))# 
print('126. ',func6(0,'*',3))#
print('127. ',func6(3,'*',0))#
print('128. ',func6(0,'*',0))# 
print('129. ',func6(2,'/',3))#
print('130. ',func6(0,'/',3))#
print('131. ',func6(4,'/',0))# 
print('132. ',func6(2,'%',3))# 
print('133. ',func6(0,'-',3))#
print('134. ',func6(2,'+',0))#  
print('135. ',func6(0,'^',0))#
 


















