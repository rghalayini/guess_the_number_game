from random import randint

def guess_number():
    number = randint(1,11)
    
    keep_asking = True

    while keep_asking:
    #chosen_numbers=[]
    #for x is not in chosen_numbers:
        x=int(input("Guess a number"))
        if number == x:
            print("You have guessed right, congratulations")
            keep_asking = False
        elif x < number:
            print("Wrong, your choice is too low, guess again")
            #chosen_numbers.append(number)
        else:
            print("Wrong, your choice is too high, guess again")
            #chosen_numbers.append(number)
        
guess_number()
 