# Asks the user for a number
get_number = int(input("Choose a number? "))

# Multiply the number by 5
times_five = get_number * 5

# Output the result
answer = ("{} times fives equals to {}"
      .format(get_number, times_five))

print(answer)

# Count up from 1 to 10...
print("counting from one to ten")
for item in range(1,11):
  print(item)

# Count down from 1 to 10...
print("counting from ten to one")  
for item2 in range(10, 0, -1):
  print(item2)

#greeting
greeting = "hello world"

for letter in greeting:
  print(letter)

#options
options = ["unicorn","horse","zebra","donkey"]

for animals in options:
  print(animals)

#get name until exit code is entered...
name = ""
while name.lower() !="xxx":
  name = input("who are you? ")
  print(name)

print()
print("We are done!")