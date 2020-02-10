y = input("enter a sentence:")

vowels=0
consonant=0
digit=0
specailchar=0

for x in y:
    if x.isalpha():
        if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
            vowels +=1

        else:
            consonant+=1

    elif x.isdigit():
        digit+=1

    else:
        specailchar+=1

print("vowels=",vowels)
print("conspnant=",consonant)
print("digit=",digit)
print("specailchar",specailchar )


