import random

print("╭── ⋅ ⋅ ── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ──╮\n  Welcome to the Lucky Unicorn Game!\n╰── ⋅ ⋅ ── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ──╯\n")

def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()

    # if they say yes, output 'program continues'
    if response == "yes" or response == "y":
      response = "yes"
      return response
      
    #if they say no, output 'display instructions'
    elif response == "no" or response == "n":
      response = "no"
      return response 
    
    else:
      print("Please answer either yes / no\n")

def instructions():
  print("\n#####################################################\n#################### How to Play ####################\n#####################################################")
  print()
  print("✦ Choose a starting amount: mininum $1, maximum $10")
  print("✦ <Enter> to start a round!")
  print("✦ How lucky can you be?")
  print("✦ Have fun!")
  
  return ""

def num_check(question, low, high):
  
  error = "Please enter a whole number between 1 and 10\n"
  
  valid = False
  while not valid:
    try:
      # asks the question
      response = int(input(question))
      # if the amount is too low / too high
      if low < response <= high:
        return response
    
      # output error
      else:
        print(error)
        
    except ValueError:
      print(error)

# Main Routine goes here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
  instructions()
print()

print("╔═════════════════════ ≪ °❈° ≫ ═════════════════════╗\n==================== Let's begin! ===================\n╚═════════════════════ ≪ °❈° ≫ ═════════════════════╝\n")
how_much = num_check("How much would you like to play with? $", 0 , 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

  # increase # of rounds played
  rounds_played += 1

  # print round number
  print()
  print("****************\n*** Round #{} ***\n****************".format(rounds_played))

  chosen_num = random.randint(1, 100)

  # adjust balance
  # if the random # is between 1 and 5,
  # user gets a unciorn (add $4 to balance)
  if 1 <= chosen_num <= 5:
    chosen = "unicorn"
    balance += 4
  # if the random # is between 6 and 36,
    # user gets a donkey (subtract $1 to balance)
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    balance -= 1
  else:
    # if the number is even, set chosen_num
    # item to a horse
    if chosen_num % 2 == 0:
      chosen = "horse"
    # otherwise set to zebra
    else:
      chosen = "zebra"
      balance -=0.50
  print()
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  print("You got a {}. Your balance is ${:.2f}".format(chosen,balance))
  print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
  if balance < 1:
    play_again = "xxx"
    print("Sorry, you have ran out of money")
  else:
    play_again = input("Press <Enter> to play again or type 'xxx' to quit ")

print()
print("Final Balance: ", balance)