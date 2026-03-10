def func():
    print("select operation: ")
    print("\n[1]add")
    print("\n[2]subtract")
    print("\n[3]multiply")
    print("\n[4]divide\n")
    
    user = int(input("enter choices: "))
    if user == 1:
    	a = int(input("enter 1st number: "))
    	b = int(input("enter 2nd number: "))
    	result = a+b
    	print("result is: ", result)
    	    	
    elif user == 2:
    	a = int(input("enter 1st number: "))
    	b = int(input("enter 2nd number: "))
    	result = a-b
    	print("result is: ", result)
    	
    elif user == 3:
    	a = int(input("enter 1st number: "))
    	b = int(input("enter 2nd number: "))
    	result = a*b
    	print("result is: ", result)
    	
    elif user == 4:
    	a = int(input("enter 1st number: "))
    	b = int(input("enter 2nd number: "))
    	result = a/b
    	print("result is: ", result)
    else:
     	print("wrong password")
func()