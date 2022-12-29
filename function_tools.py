'''
 Assignment No.: 2
 Course: PROG12974
 Name: Orlando Companioni
 Submission date:2022-11-15

Program full of usable functions for other programs
it has a power function which takes in a base and an exponent

it has a a factorial function and a special sum function which 
returns a sum of a power/factorial recursively

'''
#recursive power function
def power(num1,num2:int)->int:  
    if num2==0:            #any number to the power of 0 is 1
        return 1
    else:
        return num1*power(num1,num2-1)  #num2 controls how many times it executes

def factorial(num:int)->int: #recursive factorial function
    if num<=1:
        return 1
    else:
        return num*factorial(num-1) # will run until num is <=1, with each call of the function num goes down 

def series(num:int)->float: #recursive sum function
    if num<=0:
        return 0
    else: return power(num,num)/factorial(num)+series(num-1)   
#adds the power of num/num factorial+ itself but as a lower num,until its = to 0 or less

