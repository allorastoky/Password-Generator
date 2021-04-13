import pyperclip
import random
import os
import time
os.system("CLEAR")
password=""
x=0
menu= "1. Generate a password\n2. View password already generated\n3. Quit\n\n"
passwordused=open("used_password.txt").readlines()
letters =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["|", "!", "£", "$", "%", "&", "/", "(", ")", "=", "?", "^", "'", "[", "]", "{", "}", "*", "+", "@", "°", "#", "§", "-", "_", ".", ":", "·", "•", ",", ";", "<", ">"]
menugenerator="You can choose:\n1. A password with just letter (CAPITAL and lowercase).\n2. A password with letter (CAPITAL and lowercase) and numbers.\n3. A password with letter (CAPITAL and lowercase), numbers, and symbols (es. @, $, !, ecc...).\n\n"
possiblechoices= ["1", "2", "3"]
choice=""
choicemenu=""
while choicemenu != 3:
  while choicemenu not in possiblechoices:
    print(menu,"\n")
    choicemenu= input("What do you need. Type 1, 2, OR 3: ")
    print("\n")
  choicemenu=int(choicemenu)
  if choicemenu==1:
    while choice not in possiblechoices:
      print(menugenerator, "\n")
      choice= input("Select the kind of password you need. Type 1, 2, OR 3: ")
      print("\n")
    choice=int(choice)
    while True:
      try:
        print("\n")
        numbercharacter = int(input("Digit how many characters you password must have: ")) 
        if numbercharacter>=20:
            print("Your password will have ", numbercharacter, " characters.")
            break
        else:
          print("\n")
          print("In order to create a safe password, please insert a number greater or equal to 20.")      
      except ValueError:
        print("\n")
        print("Provide an integer value...")
        continue
    if choice==1:
      while x<numbercharacter:
        x+=1
        element=random.choice(letters)
        password+=str(element)
      print("The generate password is: ", password, ".\n \nIt has already been copied into clipboard for you! \n \n")
      passwordused.append(password)
      open("used_password.txt").write(password)
    elif choice==2:
      while x<numbercharacter:
        x+=1
        chosenlist=random.randint(1, 2)
        if chosenlist==1:
          element=random.choice(letters)
          password+=str(element)
        elif chosenlist==2:
          element=random.choice(numbers)
          password+=str(element)
      print("The generate password is: ", password, ".\nIt has already been copied into clipboard for you!")
      passwordused.append(password)
    elif choice==3:
      while x<numbercharacter:
        x+=1
        chosenlist=random.randint(1,3)
        if chosenlist==1:
          element=random.choice(letters)
          password+=str(element)
        elif chosenlist==2:
          element=random.choice(numbers)
          password+=str(element)
        elif chosenlist==3:
          element=random.choice(symbols)
          password+=str(element)
      print("The generate password is: ", password, ".\nIt has already been copied into clipboard for you!")
      passwordused.append(password)
    
      
    x=0
  pyperclip.copy(password)
print("\n\n Thanks for having used our password generator! Stay safe and see you again soon...\n\n\n\n\n")