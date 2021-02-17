import pyperclip
import random
password=""
x=0
letters =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["|", "!", "£", "$", "%", "&", "/", "(", ")", "=", "?", "^", "'", "[", "]", "{", "}", "*", "+", "@", "°", "#", "§", "-", "_", ".", ":", "·", "•", ",", ";", "<", ">"]
print("You can choose:\n1. A password with just letter (CAPITAL and lowercase).\n2. A password with letter (CAPITAL and lowercase) and numbers.\n3. A password with letter (CAPITAL and lowercase), numbers, and symbols (es. @, $, !, ecc...).")
possiblechoices= ["1", "2", "3"]
choice=""
while choice not in possiblechoices:
    choice= input("Select tha kind of password you need. Type 1, 2, OR 3: ")
    print("\n")
choice=int(choice)
while True:
  try:
    numbercharacter = int(input("Digit how many characters you password must have: ")) 
    if numbercharacter>=20:
        print("Your password will have ", numbercharacter, " characters.")
        break
    else:
      print("In order to create a safe password, please insert a number greater or equal to 20.")      
  except ValueError:
    print("Provide an integer value...")
    continue
if choice==1:
    while x<numbercharacter:
        x+=1
        element=random.choice(letters)
        password+=str(element)

print(password)
pyperclip.copy(password)