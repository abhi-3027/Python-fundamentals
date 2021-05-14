# Strings
'''
Strings are sequence of characters
the are enclosed in " " or ' '
multiline strings can be made by using """ 

Proprties:
	1 Strings can be added to other strings (concatenation)
	  e.g. 'I' + 'Love' + 'You'
	2 Strings can be multiplied
	  e.g. name = 'bob'
	       name*5 -> bobbobbobbobbob
	3 Strings can be iterated like numbers
	  e.g. name += ' is cool'
	       name -> 'bob is cool'

'''

a = 'merry'

b = 'christmas'

message = a + ' ' + b

print(message)

message += '!'

print(message)

long_message = message*5
print(long_message)


'''
Python strings can be indexed.the first character of the string is at index 0.
Characters of the string can be indexed in two ways -- left to right, which starts at 0
													-- right to left, which starts at -1


   0  1  2  3  4  5  6  7  8  9  10
   p  y  t  h  o  n  i  s  f  u  n
 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
'''

#Slicing of strings


'''
you can access a characters within a range of indicies in a string and get a "slice"/substring of that string.
Slicing syntax :

string[start_index: end_index]

NOTE: the returnes substring doesn't include the character at the end index.

python allows to omit the start or end index when slicing a string:
e.g. string = 'foobar'
     string[3 : ] -> 'bar'
     string [ : 3] -> 'foo'

'''

#Length function
'''
You can get the length of the string by using the built-in len() function, which takes a string as its parameter and returns an integer,

question = 'how are you?'
len(question) -> 12 ---> length of the string


'''

# Strings are immutable

# String Interpolation
'''
 these strings are prefixed with an f to denote how they are meant to be interpreted 

 e.g.   pie = 3.14
 		f" I ate some {pie}"  --> I ate some 3.14


 we can use str.format() method for doing the same

 % formatting - another method of interpolation

'''