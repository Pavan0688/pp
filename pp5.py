num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("enter which operation would you like to perform?")
ch=input("enter any of these char for specific operation +,-,*,/:")
result=0
if ch=='+':
    result=num1+num2
else if ch=='-':
    result=num1-num2
else if ch=='*':
    result=num1*num2
else if ch=='/':
    result=num1/num2
else:
    print("input character is not recignised!")
print(num1,ch,num2,":",result)    
