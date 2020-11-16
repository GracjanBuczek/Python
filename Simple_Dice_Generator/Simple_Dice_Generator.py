import random

#part1 Throw_A_Dice Generator
dice = random.randint(1,6)

print ('Numbers of points on dice is',dice)
if dice == 1:
    print (\
        '''

    0
   
''')
elif dice == 2:
        print (\
        '''
        0

    0      
''')
elif dice == 3:
        print (\
        '''
        0
    0
0   
''')
elif dice == 4:
        print (\
        '''
0      0


0      0
''')
elif dice == 5:
        print (\
        '''
0      0
    0
0      0
''')
elif dice == 6:
        print (\
        '''
0    0
0    0
0    0    
''')
else:
    print ('There must have happened something very bad that a different number had come up. Try once again!')

#part2 Throw_Many_Dices Generator
dices = []
roll = random.randint(1,6)
i=0

while i != 5:
    print('Next result is:', roll)
    i=i+1
    dices.append(roll)
    roll = random.randint(1,6)

print('\nOrderly sorted results of last 5 tries are:',sorted(dices))
input('\nPress any key to finish...')
