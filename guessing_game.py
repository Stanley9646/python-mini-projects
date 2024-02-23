print("lets play a game")

game=input("Do you want to play the game? ")

if game.lower() != "yes":
    quit()

print("okay let's play")
score=0

answer = input("Who is the goat? ")
if answer.lower() == "messi":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("Which is the best team? ")
if answer.lower() == "manu":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("Which is the best car? ")
if answer.lower() == "mercedes":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("devops or web development? ")
if answer.lower() == "devops":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct")

print("average of " + str((score/4) * 100) +"%")


