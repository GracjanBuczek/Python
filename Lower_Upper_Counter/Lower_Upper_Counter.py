x = input("Enter sentence: ")
count={"Uppercase":0, "Lowercase":0}
for i in x:
    if i.isupper():
        count["Uppercase"]+=1
    elif i.islower():
        count["Lowercase"]+=1
    else:
        pass
print ("There is:", count["Uppercase"], "uppercases.")
print ("There is:", count["Lowercase"], "lowercases.")
