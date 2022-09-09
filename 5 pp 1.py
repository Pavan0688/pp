print ("enter the marks obtained in 5 subjects")
markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

tot = markone + marktwo + markthree + markfour + markfive
avg = tot/5
if   avg>=91 and avg<=100:
     print("your grade is A1")
elif avg>=81 and avg<90:
     print("your grade is A2")
elif avg>=71 and avg<=80:
     print("your grade is B1 ")
elif avg>=61 and avg<=70:
     print("your grade is C1")
elif avg>=51 and avg<=60:
     print("your grade is D1")
elif avg>=0 and avg <=50:
     print(" FAIL")
else:
     print("invalid input !")
