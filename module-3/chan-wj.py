# William Judd
# 6/21/2026
# Module 3.2 Assignment
# Purpose - Chohan Revisions

# Description:
# This program is a modified version of the Cho Han dice game. The user starts
# with a purse of mon, places a bet, chooses Cho or Han, and then two dice are
# rolled. Cho means the total is even. Han means the total is odd.

# Documented changes made for Module 3.2:
# 1. Changed the input prompt to my initials followed by a colon: wj:
# 2. Changed the house percentage from 10 percent to 12 percent.
# 3. Added a program introduction notice explaining that a roll total of 2 or 7
# gives the user a 10 mon bonus.
# 4. Added logic that checks whether the dice total is 2 or 7. If true, the
# program displays a bonus message and adds 10 mon to the user's purse.


import random

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

HOUSE_PERCENTAGE = 0.12
BONUS_AMOUNT = 10
BONUS_ROLLS = (2, 7)


def get_bet(purse):
    """Prompt the user for a valid bet amount or QUIT."""
    while True:
        print(f'You have {purse} mon. How much do you bet?')
        bet = input('wj: ').strip()

        if bet.upper() == 'QUIT':
            return 'QUIT'

        if not bet.isdecimal():
            print('Please enter a number or QUIT.')
            continue

        bet = int(bet)
        if bet <= 0:
            print('You must bet at least 1 mon.')
        elif bet > purse:
            print('You do not have enough mon to make that bet.')
        else:
            return bet


def get_choice():
    """Prompt the user to choose Cho or Han."""
    while True:
        print('Do you bet on Cho, which means even, or Han, which means odd?')
        choice = input('wj: ').strip().upper()

        if choice in ('CHO', 'HAN'):
            return choice

        print('Please enter CHO or HAN.')


def roll_dice():
    """Roll two six sided dice and return both dice values."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


def main():
    """Run the Cho Han game."""
    purse = 5000

    print('''Cho Han

In this traditional Japanese dice game, two dice are rolled in a bamboo cup.
The dealer asks whether the total will be Cho, which means even, or Han, which
means odd.

If the dice roll total is 2 or 7, you receive a 10 mon bonus.
Enter QUIT instead of a bet amount to stop playing.
''')

    while purse > 0:
        bet = get_bet(purse)
        if bet == 'QUIT':
            print('Thanks for playing!')
            break

        choice = get_choice()

        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the dice.')
        print('The dealer asks for your bet.')
        print(f'You bet {bet} mon on {choice}.')
        print('The dealer lifts the cup to reveal:')

        dice1, dice2 = roll_dice()
        total = dice1 + dice2
        print(f'  {JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}')
        print(f'  {dice1} - {dice2}')
        print(f'The total roll is {total}.')

        if total % 2 == 0:
            correct_answer = 'CHO'
        else:
            correct_answer = 'HAN'

        player_won = choice == correct_answer

        if player_won:
            house_fee = int(bet * HOUSE_PERCENTAGE)
            winnings = bet - house_fee
            purse += winnings
            print(f'You won! You take {winnings} mon.')
            print(f'The house collects a {house_fee} mon fee.')
        else:
            purse -= bet
            print(f'You lost! You lose {bet} mon.')

        if total in BONUS_ROLLS:
            purse += BONUS_AMOUNT
            print(f'The total roll was {total}, so you get a {BONUS_AMOUNT} mon bonus!')

        print()

    if purse <= 0:
        print('You have run out of mon!')

    print(f'You leave with {purse} mon.')


if __name__ == '__main__':
    main()
