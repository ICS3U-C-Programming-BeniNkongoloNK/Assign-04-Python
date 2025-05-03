#!/usr/bin/env python3
# Created By: Beni
# Date: May 2, 2025
# Choose one of 2 games to play

import random


def main():

    valid_input = False

    print(
        "Hello, user. It is me again, the magic ball! I have two new games for you to play."
    )
    while valid_input == False:

        games = input("Please press 1 or 2:\n")

        try:
            games_int = int(games)

            # Rock paper scissors program
            if games_int == 1:
                # Stop try catch from repeating
                valid_input = True

                # Explain how to play
                print("Time to play rock, paper, scissors!!!")
                print(
                    "The rules are simple, type in 1(rock), 2(paper) or 3(scissors) and see if u win!"
                )
                print("Good luck!")

                # Ask user for their choice
                user_plays = input("Play \n1. Rock \n2. Paper \n3. Scissors\n")

                ai_choice = random.randint(1, 3)

                # If they choose 1 or rock
                if user_plays == "1" or user_plays == "rock":
                    if ai_choice == 1:
                        print("You both play rock and tie!!")
                    if ai_choice == 2:
                        print(
                            "Your rock is suffocated in the paper(cuz that somehow works?) and you lose!!"
                        )
                    if ai_choice == 3:
                        print(
                            "Your rock destroys the pair of scissors, giving u the win!!!!!"
                        )

                # If they choose 2 or paper
                if user_plays == "2" or user_plays == "paper":
                    if ai_choice == 1:
                        print("Paper beats rock, you win!")
                    if ai_choice == 2:
                        print("You both play paper and tie!!")
                    if ai_choice == 3:
                        print("You're torn to shreds by scissors, you lose!")

                # If they choose 3 or scissors
                if user_plays == "3" or user_plays == "scissors":
                    if ai_choice == 1:
                        print("You're destroyed by the rock, you lose")
                    if ai_choice == 2:
                        print("You dispose of paper with ease, you win")
                    if ai_choice == 3:
                        print("You both play scissors and tie")

            # Coin flip game
            elif games_int == 2:
                # Stop try catch from repeating
                valid_input = True

                # Explain how the coin flip game works
                print("Looks likes we're flipping a coin!!!")
                print(
                    "The games is simple, choose heads or tails and then choose how many times to flip."
                )
                print("If you get more of your side than the other, you win!")

                good_input = False
                while good_input == False:
                    heads_or_tails = input("Heads or tails?\n")

                    # If you choose heads it asks for how many coin flips you want
                    if heads_or_tails == "heads" or heads_or_tails == "Heads":
                        good_input = True
                        coin_flips = int(input("how many flips do you want?\n"))

                        # Sets two variables, heads and tails to 0
                        heads = 0
                        tails = 0

                        # The for loop repeats as many times as the user chose to flip the coin
                        for counter in range(coin_flips):
                            # Choose 1 or 2, 1 means heads 2 means tails
                            coin = random.randint(1, 2)

                            # Within the loop, if you get a 1, heads goes up by 1
                            if coin == 1:
                                print("Heads")
                                heads += 1
                            # Within the loop, if you get a 2, tails goes up by 1
                            if coin == 2:
                                print("Tails")
                                tails += 1

                        # If you get more heads than tails, you win
                        if heads > tails:
                            print("You guessed heads, and WON!!!")
                        # If heads and tails are equal, then play a tiebreaker
                        if heads == tails:
                            print(
                                "It was a tie, lets flip 1 more coin to do a tiebreaker"
                            )
                            # Set a last flip variable to flip 1 more time
                            last_flip = random.randint(1, 2)
                            # If the last flip is heads then you win
                            if last_flip == 1:
                                print("YOU WON THE TIEBREAKER")
                            # Else it is tails and you lose
                            else:
                                print("Unlucky, you lose")
                        # If heads is less than tails, you lose
                        if heads < tails:
                            print("You lost this time!")

                    # If you choose tails it asks for how many coin flips you want
                    elif heads_or_tails == "tails" or heads_or_tails == "Tails":
                        good_input_input = True
                        coin_flips = int(input("how many flips do you want?\n"))

                        # Sets two variables, heads and tails to 0
                        heads = 0
                        tails = 0

                        # The for loop repeats as many times as the user chose to flip the coin
                        for counter in range(coin_flips):
                            # Choose 1 or 2, 1 means heads 2 means tails
                            coin = random.randint(1, 2)

                            # Within the loop, if you get a 1, heads goes up by 1
                            if coin == 1:
                                print("Heads")
                                heads += 1
                            # Within the loop, if you get a 2, tails goes up by 1
                            if coin == 2:
                                print("Tails")
                                tails += 1

                        # If you get more tails than heads, you win
                        if heads > tails:
                            print("You lost this time!")
                        # If heads and tails are equal, then play a tiebreaker
                        if heads == tails:
                            print(
                                "It was a tie, lets flip 1 more coin to do a tiebreaker"
                            )
                            # Set a last flip variable to flip 1 more time
                            last_flip = random.randint(1, 2)
                            # If the last flip is tails then you win
                            if last_flip == 2:
                                print("YOU WON THE TIEBREAKER")
                            # Else it is heads and you lose
                            else:
                                print("Unlucky, you lose")
                        # If tails is less than heads, you lose
                        if heads < tails:
                            print("You guessed tails, and WON!!!")
            else:
                print("That is not a 1 or 2, please try again")

        except Exception:
            print("That is not a valid input")


if __name__ == "__main__":
    main()
