import random

top_of_range = input("Type a number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("type a number bigger than zero")
        quit()
else:
    print("enter a digit")

random_number = random.randint(0, top_of_range)
guesses =0
while True :
    user_guess= input("make a number guess")
    guesses+=1

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number next time')
        continue
    if user_guess == random_number:
        print("you won")
        break
    elif  user_guess > random_number:
        print("you are above the random number")
    else :
      
        print("you are below the random number")

print("you got it in" , guesses , "guesses")