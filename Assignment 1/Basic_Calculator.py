print("------------------------------------------------------------")
num1=float(input('Enter Operand 1 :'))
print("------------------------------------------------------------")
num2=float(input('Enter Operand 2 :'))
print("------------------------------------------------------------")
print("/ = Division")
print("* = Multiplication")
print("+ = Addition")
print("- = Subtraction")
print("% = Modulus")
op=input('Enter Operator:')
print("------------------------------------------------------------")
if op=='+':
    print('\nResult of Adding Numbers '+ str(num1) + ' and ' + str(num2) + ' is : ' + str(num1+num2))
    print("------------------------------------------------------------")
elif op=='-':
    print('\nResult of Subtracting Numbers '+ str(num1) + ' and ' + str(num2) + ' is : ' + str(num1-num2))
    print("------------------------------------------------------------")
elif op=='*':
    print('\nResult of Multiplying Numbers '+ str(num1) + ' and ' + str(num2) + ' is : ' + str(num1*num2))
    print("------------------------------------------------------------")    
elif op=='/':
    print('\nResult of Dividing Numbers '+ str(num1) + ' and ' + str(num2) + ' is : ' + str(num1/num2))
    print("------------------------------------------------------------")    
elif op=='%':
    print('\nResult of Moduling Numbers '+ str(num1) + ' and ' + str(num2) + ' is : ' + str(num1%num2))
    print("------------------------------------------------------------")
else:
    print('\n"Invalid Operation Requested!"')
print("------------------------------------------------------------")