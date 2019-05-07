# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

i = 1

while i == 1:
    first_player = input("please Start the game :")
    second_player = input("second guy its your turn now:")

    if first_player == "Rock" and second_player == "Scissors":
        print("player one wins; he is ", first_player)
        print("DO you want to play again? (Yes or No)")
        play_again = input()
        if play_again == "Yes" or play_again == "yes":
            i = 1
        else:
            i = 0
    elif first_player == "Rock" and second_player == "Paper":
        print("player two wins; he is ", second_player)
        print("DO you want to play again? (Yes or No)")
        play_again = input()
        if play_again == "Yes" or play_again == "yes":
            i = 1
        else:
            i = 0
    elif first_player == "Scissors" and second_player == "Rock":
        print("player two wins; he is ", second_player)
        print("DO you want to play again? (Yes or No)")
        play_again = input()
        if play_again == "Yes" or play_again == "yes":
            i = 1
        else:
            i = 0
    elif first_player == "Scissors" and second_player == "Paper":
        print("player one wins; he is ", first_player)
        print("DO you want to play again? (Yes or No)")
        play_again = input()
        if play_again == "Yes" or play_again == "yes":
            i = 1
        else:
            i = 0
    elif first_player == "Paper" and second_player == "Rock":
        print("player one wins; he is ", first_player)
        print("DO you want to play again? (Yes or No)")
        play_again = input()
        if play_again == "Yes" or play_again == "yes":
            i = 1
        else:
            i = 0
    elif first_player == "Paper" and second_player == "Scissors":
        print("player two wins; he is ", second_player)
        print("DO you want to play again? (Yes or No)")
        play_again = input()
        if play_again == "Yes" or play_again == "yes":
            i = 1
        else:
            i = 0
