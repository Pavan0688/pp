strl = input("please enter your own string : ")
vowels=0
consonants=0
strl.lower()
for i in strl:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowels=vowels+1
     else:
            consonants=consonants+1
print("total number of vowels in this string=",vowels)
print("total number of consonants in this string=",consonants)
