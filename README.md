# vision_lab
A collection of projects, experiments, and ideas built while learning Computer Science, AI, and software development.
second project=dice rolling game
import random 

while True:
    choice=input(str('Roll the dice?(y/n)=    ')).lower()
    break        
    
if choice =='y':
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f'({die1},{die2})')
elif choice=='n':
    print('thanks for playing!')    

else:        
        print('invalid choice!')

