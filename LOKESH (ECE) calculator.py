x=float(input("enter x : "))
y=float(input("enter y : "))
print(x)
print(y)
print('chose your operation')
print('1.add')
print('2.sub')
print('3.mul')
print('4.div')
while True :
    choice=input("choose (1/2/3/4) or q to quit : ")
    if choice == 'q' :
        break
   
    if choice == '1':
        print(x+y)
    elif choice == '2':
        print(x-y)
    elif choice == '3':
        print(x*y)
    elif choice == '4':
        print(x/y)
    else:
        print("your choice is invalid!")
        print("please try again")
    
    
    
       
        
    
