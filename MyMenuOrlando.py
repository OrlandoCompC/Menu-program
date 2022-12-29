'''
 Assignment No.: 2
 Course: PROG12974
 Name: Orlando Companioni
 Your Sheridan Student Number:991437087
 Submission date:2022-11-15
 Instructor's name: Syed Tanbeer

The program shows the user a menu for them too choose an option, then performs the option chosen
it utilizes functions, loops, if statements, any(), try, exception, and the use of modules
'''
import function_tools as ft # function_tools is a module with a power, factorial and a sum function


def main(): # main function
    process()
                
def process(): # does all the process for the whole program 
    choose_options=["1","2","3","4","5"]
    option_list=["a","b","A","B"]
    user_choose=""
    while user_choose!="5":
        menu()  
        user_choose=chosen_menu()     
        if not any(num in choose_options for num in user_choose):  
            # similar to a try, exception. if the input is not one of the options then it will output the menu again 
            print(" Invalid option, please enter one of the options from the menu")
            continue
        elif user_choose=="1":
            option=input(f"Please choose option a or b: ") #allows the user to choose between triangle and square
            if not any(letter in option_list for letter in option):
                print("Invalid option, please enter one of valid letter options")
                continue
            elif option.lower()=="a":
                try:
                    height=int(input(f"Enter the height of the Triangle(Positive integers only): "))

                    draw_triangle(height)
                except Exception as e:
                    print("Invalid value")
                    continue
            elif option.lower()=="b":
                try:
                    row=int(input(f"Enter length of the Rectangle(Positive integers only): "))
                    column=int(input(f"Enter the width of the rectangle(Positive integers only): "))
                    draw_rectangle(row,column)
                except Exception as p:
                    print("Invalid value")
                    continue
            else:print("Invalid option")
        elif user_choose=="2":
            is_fermat()
        elif user_choose=="3":
            try:
                number=int(input(f"Please Enter a non negative integer: "))
                if number<0:
                    print("Invalid value, Please try again")
                else:
                    sum=facto_power(number)
                    print(f"The sum of the series is {sum}")
            except Exception as m:print("Invalid input, Please try again")
        elif user_choose=="4":
            password()
        elif user_choose=="5":
            print("Thank you for using my menu program, Goodbye")
            break
            
def menu():# displays the menu
    print('''
    1 - Draw Shape
    a) Triangle
    b) Rectangle
    2 - Fermat's Last Theorem
    3 - Facto-Power Series
    4 - Check Password
    5 - Quit''')

# function that takes the user input of the menu
def chosen_menu()->str:
    user_choose=input(f"Enter a number to choose an option from the menu: ")
    return user_choose

# functions used if the user enters 1 then enters a
def draw_triangle(rows:int):
      
    for row in range(rows): 
        
        for column in range(row+1):   # +1 because if not it wont print a row 
            if column==0 or column==row or row==rows-1:
                #checks if column==0 because thats the first line that has to print
                #when row==rows-1 is the last horizontal line that has to print in full

                    print("*",end=" ")    
            else:
                print(" ",end=" ")  # will print the blank spaces in between if its not one of the edges
            
        print()
      
# functions used if the user enters 1 then enters b
def draw_rectangle(rows,columns:int):

    for row in range(rows):
        
        for column in range(columns):  
            if  row == 0 or row==rows-1 or column==0 or column==columns -1:
            #when row is 0 is the first row, when row is rows-1 is the last row
            #when column is 0 is the first column, when column is columns-1 is the last column

                    print("*",end=" ")    
            else:
                print(" ",end=" ") # if its not the first or the last then print spaces in between
            
        print()

# functions used if the user enters 2
def is_fermat():
    try:
        #provides values to the variables
        a_value=int(input("Enter a non-negative integer for a: "))
        b_value=int(input("Enter a non-negative integer for b: "))
        c_value=int(input("Enter a non-negative integer for c: "))
        n_value=int(input("Enter a non-negative integer for n: "))
        value_list=[a_value,b_value,c_value,n_value]
        if any(val <0 for val in value_list):# checks of the values are negatives and if they are it calls main()
            print("Invalid negative number entered, please try again")
        else:
            #checks if n is >2 then it checks if the theory stays true
            #uses the power function inside the function.tools module
            if n_value>2 and ft.power(a_value,n_value)+ft.power(b_value,n_value)!=ft.power(c_value,n_value):
                print(f"For n = {n_value}, Left hand side != Right hand side: The theorem holds")

            elif n_value<=2 and ft.power(a_value,n_value)+ft.power(b_value,n_value)!=ft.power(c_value,n_value):
                print(f"For n = {n_value}, Left hand side != Right hand side: The theorem holds")
            else:
                print(f"For n = {n_value}, Left hand side = Right hand side: The theorem holds")
            #for any value of n, <=2 then the theory will hold regardless
    except Exception as e:print("Invalid value, Please try again")
        

# functions used if the user enters 3
def facto_power(number:int)->float: 
    # uses the power function, the factorial function and the sum function inside function.tools
    sum=ft.series(number)
    return sum
    
#the function used when the user inputs 4
def password():
    user_password=input(f"Please enter a password: ")
    symbol_list= ["~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]","|",":",";","'","?"]
    #symbol_list has a list of symbols a user might use
    
    invalid_symbol=["<",">"] # these are the symbols users cant use 
    valid_pass=1   #turns 0 when the password is invalid in any way
    pass_length=len(user_password)

    # If the password doesnt contain letters then it becomes 0
    contains_letter=1
    
#did not use nested ifs because i wanted it to check all conditions and tell the user what they needed to add

    if pass_length<=8: # checks if the length of the password is less than or equal to 8
        valid_pass = 0   
        print(f"Invalid password. Password length must be at least 8 characters long.")

# any will return true if there is an invalid character in the password
    if  any(char in invalid_symbol for char in user_password):  #any returns True or False
        valid_pass=0          
        print(f"Invalid password. Password should not contain '<' and '>'.")
              
    # the not operator makes it so that if it doesnt have a digit then it executes
    if not any(char.isdigit() for char in user_password):
        #it iterates through the password checking if it has digits

        valid_pass=0
        print(f"Invalid password. Password must contain at least 1 number")

    if not any(char.isalpha() for char in user_password):
        valid_pass=0
        contains_letter=0
        print(f"Invalid password. Password must contain at least 1 letter")
        
    if not any(char in symbol_list for char in user_password):
        # in this case it compares characters in a list to those the password
        valid_pass=0
        print(f"Invalid password. Password must contain at least 1 symbol")      

    if not any(char.isupper() for char in user_password) and contains_letter==1:
        # if it doesnt contain letters then it doesnt execute because only letters can be upper or lowercase
        valid_pass=0

        print("Invalid password. Password must contain at least 1 uppercase letter")
          
    if not any(char.islower() for char in user_password) and contains_letter==1:
        valid_pass=0
        print("Invalid password. Password must contain at least 1 lowercase letter")
        
    if valid_pass==1:# if its still valid then it prints that it is
        print(f"The Password is valid")
 

try: 
    main()
except KeyboardInterrupt: # if the user presses ctrl+c it will exit the program without an error 
    print("Program closed")