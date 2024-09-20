print("Winners and Losers - Human is Even, Computer is Odd ")
#from random import randint x = randint(1,5)

import random
rounds = 5
Human = 0
Computer = 0


for Round in range(1, 6):
    Human_Guess = int(input(f"Round {Round}: \nEnter your Guess: "))
    Computer_Guess = random.randint(1, 5)
    total = Human_Guess + Computer_Guess

    print(f"Human Guess: {Human_Guess} - Computer Guess: {Computer_Guess}")

    if total % 2 ==0:
        print("Sum is Even")
    else:
        print("Sum is Odd")
    
    if total % 2 ==0:
        Human += 1
        print(f"Human Score: {Human} - Computer Score: {Computer}")
        

    else:
        Computer +=1
        print(f"Human Score: {Human} - Computer Score: {Computer}")
        
    if Human > Computer:
        print("Human Wins!")
    else:
        print("Computer Wins!")

   

