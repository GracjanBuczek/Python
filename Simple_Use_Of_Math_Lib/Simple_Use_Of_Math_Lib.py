import math
idt = [0,1,2,3,5,8,13,21,34,55,89]
fcb = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

print ('Amount of elements in inputdata is:',len(idt))
print ('Amount of elements in factortabele is:',len(fcb))

if len(idt)==len(fcb):

    n=int(input("\nChoose any element from inputdata: "))
    if n> len(idt):
             n=int(input("Chosen number is too high.\nPlease choose it again: "))

    minvalue=(idt[n]-fcb[n]*idt[n])
    print ("\nMinimal value:", minvalue)

    maxvalue=(idt[n]+fcb[n]*idt[n])
    print ("Maximal value:", maxvalue)

    print ("\nMinimal intiger value:", math.floor(minvalue))
    print ("Maximal intiger value:", math.ceil(maxvalue))
    print ("\nAnswer for task number 9 is:", math.floor(minvalue), idt[n], math.ceil(maxvalue))

else:
    print ("Inputdata [idt] and factortable [fcb] need to have equal number of elements")

input ("\nPress any key to finish...")
