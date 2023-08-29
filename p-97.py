import random 
print("Number guessing game")
number=random.randint(1, 9)
chances=0
print("Guess a number between(1,9)")

while chances < 5:
 guess=int(input("Enter ur guess"))
 if guess==number:
    print("congratulation u win")
    break

 elif guess < number:
    print("your guess was too low: Guess a higher than",guess)
 else:
     print("your guess was too high: Guess a lower than",guess)

 chances +=1


if not chances < 5:
    print("You lose!!! The number is,",number)     

