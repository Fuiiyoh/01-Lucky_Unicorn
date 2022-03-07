def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()

    # if they say yes, output 'program continues'
    if response == "yes" or response == "y":
      response = "yes"
      return response
    
    elif response == "no" or response == "n":
      response = "no"
      return response
    #if they say no, output 'display instructions'
    else:
      print("Please answer either yes / no")

def instructions():
  print("**** How to Play ****")
  print()
  print("The rules of the game go here")
  print()
  return ""
  
# Main Routine goes here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
  instructions()

print("Program continues")
