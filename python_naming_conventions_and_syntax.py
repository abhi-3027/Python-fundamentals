# Python naming conventions 


1. Compound variable names shoul be written in sanke_case notation.
 e.g. first_letter = "a"  # snake_case
 Don't do this:
 	 firstLetter = "a" #cammelCase
	 FirstLetter = "a" #PascalCase




 2. Naming of constants should be written in capital letter to denote that their values are not meant to change.

   e.g. NUMBER_OF_PLANETS = 8
        RADIUS_OF_EARTH_IN_KM = 6371




#Python Syntax


<Comments>
# --> block or inline comment

''' ''' or """ """  --> Doc string(Documentation Strings) - is a literal string used as a python comment. It is often used to document modules,functions, and class definations.

<Identation>

Blocks -->  group of statements that are executed together. fundamental aspect of programming. allow set of statements to be executed as though they were single
	e.g.

	if x>0:
		#execute this block of statements
		print('Block 1')
	else:
		#execute this block of statements
		print('Block 2')

