import random
import os

user_cards = []
computer_cards =[]
game_over = False

def deal_cards():
    """Get a random card and return the value """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(list_of_cards):
    """ Take a list of cards and return the score calculated from the cards"""
    sum_cards = sum(list_of_cards)
    if sum_cards == 21 and len(list_of_cards) == 2:
        return 0
    while sum_cards > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum_cards


def compare(u_score, c_score):
    """ Compare scores and print the result """
    if u_score == c_score:
        print("You Win!")
    elif c_score == 0:
        print("You lose!")
    elif u_score == 0:
        print("Its a Draw!")
    elif u_score > 21:
        print("You Lose!")
    elif c_score >21:
        print("You Win!")
    elif u_score > c_score:
        print("You Win!")
    elif c_score > u_score:
        print("You lose!")


#outer loop to reset game
while True:
    # name of operating system, nt = windows, posix = mac/linux so if os.name is equal to nt then it uses cls to clear the terminal otherwise it uses the clear function to clear the terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Reset game state
    user_cards = []
    computer_cards = []
    game_over = False

    
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # Inner loop for current round
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        while True:
            draw_cards = input("Do you want to draw another card? 'Yes' or 'No': ").lower()
            if draw_cards in ["yes", "y", "no", "n"]:
                break  # exit the loop if input is valid
            print("Invalid input! Please type 'Yes' or 'No'.")
        
        if draw_cards in ["yes", "y"]:
            user_cards.append(deal_cards())
        else:
            while computer_score < 17:
                computer_cards.append(deal_cards())
                computer_score = calculate_score(computer_cards)
            game_over = True

    # End of round: show results
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    # Ask to play again
    play_again = input("Do you want to play another round? 'Yes' or 'No': ").lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye 👋")
        break



