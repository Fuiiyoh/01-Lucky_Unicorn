show_instructions = ""
while show_instructions.lower() != "xxx":
  
  # asks if the user has played before
  show_instructions = input("Have you played this game before? ").lower()
  
  # if they say yes, output 'program continues'
  if show_instructions == ("yes") or show_instructions == ("y"):
    show_instructions == ("yes")
    print("program continues")
  
  elif show_instructions == ("no") or show_instructions == ("n"):
    print("Display instructions")
  #if they say no, output 'display instructions'
  else:
    print("Please answer either yes / no")