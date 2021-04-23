import random 

# List of options
names = ["rock", "paper", "scissors"]



user = input("rock, paper or scissors  ")

computer = random.choice(names)


if user == "rock" :
  computer = random.choice(names) 
  if computer == "paper" :
      print("You lose")
  if computer == "scissors" :
      print("You lose")
  if computer == "rock" :
      print("Tie computer also picked rock")

if user == "paper" :
  computer = random.choice(names) 
  if computer == "paper" :
      print("Tie computer also picked paper")
  if computer == "scissors" :
      print("You lose")
  if computer == "rock" :
      print("You win")

if user == "scissors" :
  computer = random.choice(names) 
  if computer == "paper" :
      print("You lose")
  if computer == "scissors" :
      print("Tie computer also picked scissors")
  if computer == "rock" :
      print("computer picked rock so You WIN")



    

