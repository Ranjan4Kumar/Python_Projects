
def name_ask():
  while True:
    name = input('What is your name:') # This function will only take anme as input and only characters are allowed not any funcky names.
    if name.replace("", " ").isalpha() and len(name)>3: # this line of code will check the input is alphabet and length is greater than 3.
      break # If the name is correct the code will break
    else :
      print('Error Invalid Entry :(Enter the correct name') # correction message
  return name # Returning the name value


def age_ask(): # checking if the age entered is valid
  while True:
    age = input('Enter your age:')
    if age.isnumeric() and int(age)<100: # checking the age is numeric and less than 4 digit
      break
    else :
      print('Invalid age')
  return age

def main():
  entered_name = name_ask()
  entered_age = age_ask()
  print('=========================================')
  print("Personal Details")
  print('=========================================')
  print(f" Name:{entered_name}")
  print(f" Age: {entered_age}")



