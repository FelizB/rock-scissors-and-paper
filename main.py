import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game=[rock,paper,scissors]

position=input("What do you chose? Type 0 for rock, 1 for paper or 2 for scissors\n")

position2=int(position[0])
game2=game[position2]
print("You have choosen\n",game2)
game2_comp=random.choice(game)
print("The computer has chosen\n",game2_comp)
if game2==game2_comp:
  print("You tie with computer!!")

else:
  print("You loose to the computer")