import random
number = random.randint(1, 100)

while True:
  try:
        guess =int(input("Guess a number between 1 and 100:  "))
        if guess > number:
            print("The guess is too high")
        elif guess < number:
            print("The guess is too low")
        elif guess == number:
            print("You guessed the number correctly!")
            break
  except ValueError:
   print("Invalid input please try again") 
        
    
        

