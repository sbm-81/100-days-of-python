import random
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(rock)
print(paper)
print(scissors)

options=[rock,paper,scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
userChoice=input()
if int(userChoice)>2 or int(userChoice)<0:
    print("Invalid input, you lose")
else:    
    print("You chose:")
    print(options[int(userChoice)])


randomchoice=random.randint(0,2)
print("Computer chose:")
print(options[int(randomchoice)])

if int(userChoice)>2 or int(userChoice)<0:
    print("Invalid input, you lose")
elif int(userChoice)==randomchoice:
    print("It's a draw")
elif userChoice==0 and randomchoice==2:
    print("You win")
elif userChoice==1 and randomchoice==0:
    print("You win")
elif userChoice==2 and randomchoice==1:
    print("You win")
else:
    print("You lose")