''' Numerical data '''

''' types of numbers - integers, floating point numbers, hexadecimal, octal, binary

Integers:
	comprised of whole numbers

	e.g:
		integer = 49
		neg_integer = -35
		print(type(integer), integer) -> outputs: class 'int' 49     #type(variable) -> check the data type of the variable

	python integers have unlimited precision and there is no limits to how large they can be

Floating Point Numbers:
	 decimal numbers

we can convert integers and floating to each other:
e.g. float(234) -> 234.0


binary -> system with base 2
hexadecimal -> system with base 16
octal -> system with base 8

'''

num = 23

print(bin(num)) #prints the binary value of 23

print(oct(num)) #prints the octal value of 23

print(hex(num)) #prints the hexadecimal value of 23

print(float(num)) #prints the floating point value of 23


i = int('10001' , 2) #converts binary to integer -> remember passing the string of binary is important otherwise it will give #error and second argument specifies the base of the system. pass 8 for octal;16 for hex