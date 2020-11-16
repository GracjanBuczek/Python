import random

#part 1 - Pseudorandom number generator 
for n in range (0,10):
    n = random.randint(1,100)
    print(n)
input("\nPress any key to continue...\n")
#part 2 - Comapring x&y, counter
number1 = random.randint(1,100)
number2 = random.randint(1,100)
counter = 1
while number2!=number1:
    print('Value of number1 is:',number1,', value of number2 is:',number2,'. Counter:',counter)
    counter = counter+1
    number2 = random.randint(1,100)

else:
    print('At least! After',counter,'tries it succeed!')
