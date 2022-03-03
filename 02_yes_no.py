def yes_no(question):
  valid = False
  while not valid:
    response = input(question).lower()

    # if they say yes, output 'program continues'
    if response == ("yes") or response == ("y"):
      response = ("yes")
      return response
    
    elif response == ("no") or response == ("n"):
      response = ("no")
      return response
    #if they say no, output 'display instructions'
    else:
      print("Please answer either yes / no")

show_instructions = yes_no("Have you played this game before? ")
print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("You said {} to having fun".format (having_fun))