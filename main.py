#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def game():
  choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  game_over = False
  
  if choose == "hard":
      attempts = 5
      computer_guess = random.randint(1, 100)
      
      while not game_over and attempts > 0:
          guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
          
          if guess == computer_guess:
              print(f"You won! The correct number was {computer_guess}.")
              game_over = True
          else:
              attempts -= 1
              if guess > computer_guess:
                  print("Too high.")
              else:
                  print("Too low.")
              
          if attempts == 0:
              print(f"Out of attempts. You lose. The number was {computer_guess}")
  elif choose == "easy":
    attempts = 10
    computer_guess = random.randint(1, 100)
      
    while not game_over and attempts > 0:
      guess = int(input(f"You have {attempts} attempts remaining to guess the number.\nMake a guess: "))
          
      if guess == computer_guess:
        print(f"You won! The correct number was {computer_guess}.")
        game_over = True
      else:
        attempts -= 1
        if guess > computer_guess:
          print("Too high.")
        else:
          print("Too low.")
              
        if attempts == 0:
          print(f"Out of attempts. You lose. The number was {computer_guess}")
  
  want = input("Do you want to play gain?")
  if want.lower() == "yes":
    clear()
    game()
  else: 
    clear()
game()  
      


