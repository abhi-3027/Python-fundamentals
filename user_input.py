# User Input from keyboard
'''
Input() --> allows user to type input the program
		--> execution of the program is paused until the ENTER key is pressed after user input 
		--> User Input is passed to the program as a string that can be used

'''

print("hello human. What is your name?")
name = input()

# the above two lines can be combined like:
full_name = input('please enter your full name!')


print('so ',name,' what is your age?')
age = input() # age is taken as string
age = int(age) #type casting the age to int from string
print('so next year you will be', age +1)

bin_age =  bin(age)  #converting age to binary
print('your age in binary is ', bin_age)