#Dynamic Script in python


#importing sys library to read arguments from the command line
import sys      


print('--------------------')
print('First Name: ', sys.argv[1]) #grab the first argument and print it
print('Last Name: ', sys.argv[2])  #grab the second argument and print it
print('--------------------')

'''  
The indexing is passed from 1 for grabbing the arguments because argv[0] is the name of the program file that is 
print(sys.argv[0]) --> DynamicScriptInPython.py
'''