"""The game() in a program  lets a user play a game and return the score as an integer .You need to
read a file highscore.txt ,which is either blank or store the previous highscore .You need to update
the high score whenever the game() breaks the high score

"""
import random
def game():
    print("You are entering to the game.")
    score = random.randint(1,100)
    with open("highscore.txt","r") as f:
        high_score = f.read()
        if(high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your score is{score}.")
    if(score>high_score):
        with open ("highscore.txt","w") as file:
            file.write(str(score))
    return score
game()