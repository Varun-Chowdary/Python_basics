#ROLLING DICE SIMULATOR

import random
print('****************************')
print('Welcome to the Rolling Dice game')
p=input('Press P to roll the dice or S to Stop playing')
rep=True
while rep:
    
    print(random.randint(1, 6))
    print('-----')
    print('Press P play to play again')
    rep='P' in input()
        

