# Rock,Paper and Scissor

import random
# Choice_arr=[0,1,2]
# choice=random.choice(Choice_arr)
rock='''🪨🪨'''
paper='''📃📃'''
scissor='''✂️✂️'''

game=[rock,paper,scissor]

user_choice=int(input("what do you choose? 0 for Rock, 1 for Papre, 2 for Scissor\n"))
print(f"You choose:{game[user_choice]}")
computer_choice=random.randint(0,2)

print(f"computer choose:{game[computer_choice]}")

if user_choice>3:
    print("You entered wrong number, You lose!") 
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice>computer_choice:
    print("'You win!")
elif computer_choice>user_choice:
    print("'You lose!")
elif user_choice == computer_choice:
    print("It's Draw")      
