# Main Script
import calc

flag = 'y'  #flag to exit or continue loop
commands = ['add', 'sub', 'mult', 'div']    #list of available commands

#Main Loop
while(flag.lower()!='stop'):
    #Operand Validation
    while(True):
        opt = input('Enter any command (Add/Sub/Mult/Div): ')
        if(opt.lower() in commands):
            break
        print('Please Enter a valid command')
        
    #First Number Validation
    while(True):
        num1 = input('Enter First Number: ')
        if(num1.isdigit()==True):
            num1 = int(num1)
            break
        print('Please Enter a valid number')
        
    #Second Number Validation
    while(True):
        num2 = input('Enter Second Number: ')
        if(num2.isdigit()==True):
            num2 = int(num2)
            break
        print('Please Enter a valid number')
    
    #Calculation
    if(opt.lower()=='add'):
        res=calc.Add(num1,num2)
        sign='+'
        
    elif(opt.lower()=='sub'):
        res=calc.Sub(num1,num2)
        sign='-'
    
    elif(opt.lower()=='mult'):
        res=calc.Mult(num1,num2)
        sign='*'
        
    elif(opt.lower()=='div'):
        if(num2==0):
            sign='Nan'
        else:
            res=calc.Div(num1,num2)
            sign='/'
            
    #Display
    if sign=='Nan':
        print("Can't Divide by zero")
    else:
        print(f'{num1} {sign} {num2} = {res}')
    
    
    flag = input('Enter any key to continue or "Stop" to exit: ')