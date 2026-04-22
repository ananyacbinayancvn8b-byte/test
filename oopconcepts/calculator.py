num1=int(input())
num2=int(input())
print("Enter 1 for addition\nEnter 2 for subtracton\nEnter 3 for multiplication\nEnter 4 for division")
ch=int(input())
if ch==1:
    print(num1+num2)
elif ch==2:
    print(num1-num2)
elif ch==3:
    print(num1*num2)
elif ch==4:
    print(num1/num2)
else:
    print("invalid choice")