# function goes here
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

# main routine goes here
how_much = num_check("How much would you like to pay with? ", 0 , 10)

print("You will be spending ${}".format(how_much))