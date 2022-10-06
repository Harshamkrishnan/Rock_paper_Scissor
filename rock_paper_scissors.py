#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

game_images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if player >= 3 or player < 0:
  print("You typed an invalid number you lose!!!")
else:
    print(game_images[player])

    print("Computer chose:")
    
    computer = random.randint(0,2)
    print(game_images[computer])
    
    if (computer == 0 and player == 0) or (computer == 1 and player == 1) or (computer == 2 and player == 2):
      print("Draw!!")
    elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
      print("You win!!!")
    elif (computer == 1 and player == 0) or (computer == 2 and player == 1) or (computer == 0 and player == 2):
      print("You lose!!!")


# In[ ]:




