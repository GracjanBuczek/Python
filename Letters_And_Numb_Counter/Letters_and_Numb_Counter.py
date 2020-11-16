list_ = input("Enter sentence: ")
count={"Numbers":0, "Letters":0}
for x in list_:
    if x.isdigit():
        count["Numbers"]+=1
    elif x.isalpha():
        count["Letters"]+=1
    else:
        pass
    
print ("There is ", count["Letters"], "letters and also", count["Numbers"],"numbers.")
