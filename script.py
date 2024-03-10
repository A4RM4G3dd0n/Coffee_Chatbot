# Define your functions
def order_latte():
  res = input("And what kind of milk for your latte?\n[a] 2% milk\n[b] Non-fat milk \n[c] Soy milk\n>")
  if res == 'a':
    return '2% milk'
  elif res == 'non-fat milk':
    return 'mocha'
  elif res == 'c':
    return 'soy milk'
  else:
    print_message()

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee\n[b] Mocha\n[c] Latte \n>")
  if res == 'a':
    return 'brewed Coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return "latte with " + order_latte()
  else:
    print_message()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()

def coffee_bot():
  print("Wecome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  #print(size)
  #print(drink_type)
  print("Alright, that's a", size, drink_type,"!")
  name = input("Can I get your name please? ")
  print("Thanks, " + name + "! Your drink will be ready shortly.")

# Call coffee_bot()!
coffee_bot()
