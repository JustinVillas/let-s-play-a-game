# Rock, Paper, and Scissors Game in Phyton
choices = ["rock", "paper", "scissors"]
playgame = True

while playgame == True:
    computer = choices
    player = input("Choose rock, paper, or scissors:")

    if player == computer:
        print("it's a tie")

    elif player == "rock":
        if computer == "scissors":
            print("You win! Rock smashes scissors.")
        else:
            print("You lose! Paper covers rock.")

    elif player == "paper":
        if computer == "rock":
            print("You win! Paper covers rock.")
        else:
            print("You lose! Scissors cut paper.")

    elif player == "scissors":
        if computer == "paper":
            print("You win! Scissors cut paper.")
        else:
            print("You lose! Rock smashes scissors.")

    else:
        print("Not a valid play. Try again!")
        continue

    KeepPlaying = input("Play again? ")
    playgame = False
    print("Thanks for playing")
