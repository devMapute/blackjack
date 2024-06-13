# MAPUTE ANDRAE M
# CMSC12B5L
# Final project

# This code is a standard blackjack game that employs a scoring system and a leaderboard.

import random
import time


# Function to print mainmenu
def mainmenu():
    print('\n====================================================================')
    print("██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗")
    print("██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝")
    print("██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░")
    print("██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░")
    print("██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗")
    print("╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝")
    print('====================================================================')
    print('\n\t\t\t[1] Play \n\t\t\t[2] Leaderboard \n\t\t\t[3] Exit\n')

# Function to create all cards in a standard deck


def deck():
    suits = ['\u2663', '\u2764', '\u2666', '\u2660']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    full_deck = []
    for i in suits:
        for j in cards:
            full_deck.append(j + i)

    return full_deck

# Function to append cards on player and dealer hand and remove the cards on the deck


def playingcards(deck, player_cards, dealer_cards, trigger):
    while len(player_cards) < 2:
        player_card = random.choice(deck)
        deck.remove(player_card)
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        player_cards.append(player_card)
        dealer_cards.append(dealer_card)
    # After first round, player will get 1 card only
    if trigger == 1:
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

    return [deck, player_cards, dealer_cards]

# Function to print the cards on hand of the player and the dealer


def printcards(pcards, index):
    # print(pcards)
    if index == 1:
        print('====================================================================')
        print('Your cards are:')
        print('\t', end='')
        print(' '.join(str(x) for x in pcards[index]))
        print('\n')
    elif index == 2:
        print("The dealer's cards are:")
        print('\t', end='')
        print(' '.join(str(x) for x in pcards[index]))
        print('\n')

# Function to compute the score value of the cards on hand of the player and the dealer


def hand_value(x):
    roundscore = 0
    # A dictionary for the corresponding weight per card
    cards_values = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                    "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10}
    # Variables to toggle if ace, king, queen, jack, and 10 cards exists
    aceexists = 1
    kqj10exists = 0
    # For blackjack round
    if len(x) == 2:
        for card in x:
            if card[0] == 'A':
                aceexists = 2
            elif card[0] == "K" or card[0] == "Q" or card[0] == "J":
                kqj10exists = 2
            elif card[0] == '1' and card[1] == '0':
                kqj10exists = 2
        # Blackjack combo
        if aceexists == kqj10exists:
            roundscore += 21
        # First round if blackjack combo is false
        else:
            for card in x:
                if card[0] == "K" or card[0] == "Q" or card[0] == "J":
                    roundscore += 10
                elif card[0] == '1' and card[1] == '0':
                    roundscore += 10
                else:
                    roundscore += cards_values[card[0]]
    # Computation for the following round
    else:
        for card in x:
            if card[0] == "K" or card[0] == "Q" or card[0] == "J":
                roundscore += 10
            elif card[0] == '1' and card[1] == '0':
                roundscore += 10
            else:
                roundscore += cards_values[card[0]]

    return roundscore

# Function to check if player hits a Blackjack on first round or busts on rounds after the first


def scorecheck(playerscore, round):
    flag = 0
    if round == 1:
        if playerscore == 21:
            print('You hit a Blackjack!')
            flag = 1
    else:
        if playerscore < 21:
            return flag
        elif playerscore >= 21:
            print('You bust! Game over!')
            flag = 2

    return flag

# Function to print menu of in-game options


def playerchoice():
    print('\t\t\t[1] Hit \n\t\t\t[2] Stand \n')

# Function to tell if player wants to continue or exit the ongoing game


def continuegame():
    print('\n[1] Continue \n[2] Exit')
    while True:
        choice = int(input('Enter Choice: '))
        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        else:
            continue


# Leaderboard Dictionary
leaderboard = {}

# Function to add an entry to leaderboard


def addtoleaderboard(name, score):
    leaderboard[name] = score

# Function to save the dictionary to a txt file


def saveleaderboard():
    fileHandle = open('blackjack_Leaderboard.txt', 'a')

    for i, j in leaderboard.items():
        fileHandle.write(i + ',' + str(j) + '\n')

    fileHandle.close()

# Function to import the existing leaderboard to the game


def loadleaderboard():
    try:
        fileHandle = open('blackjack_Leaderboard.txt', 'r')
        dict_loaded = {}

        for line in fileHandle:
            data = line[:-1].split(',')
            dict_loaded[data[0]] = data[1]

        fileHandle.close()
        return dict_loaded
    except FileNotFoundError:
        return {}

# Function to sort and print the leaderboard dictionary in accordance to ranking (highest to lowest)


def print_leaderboard(leaderboard):
    sorted_leaderboard = sorted(
        leaderboard.items(), key=lambda item: int(item[1]), reverse=True)
    print('\n====================================================================')
    print("{:<10}{:<10}{:<20}{:>15}".format("", "Rank", "Name", "Score"))
    print('====================================================================')
    for i, (name, score) in enumerate(sorted_leaderboard):
        print("{:<10}{:<10}{:<20}{:>15}".format("", i + 1, name, score))
    print('====================================================================\n')


# Design xD
print("\n\t\t\tYou are now playing...")
time.sleep(1)

while True:
    mainmenu()
    gamestart = False
    navigate = int(input('Press buttons to continue: '))
    if navigate == 1:
        totalpoints = 0
        round = 1
        print("\t\t\tShuffling Cards...")
        Deck = deck()
        time.sleep(2)
        print('\n')

        player_cards = []
        dealer_cards = []
        gamestart = True
        trigger = 0
        lock = False
        while gamestart == True:
            # For user error
            if lock == False:
                # Gives a new deck if deck has 10 or less than cards
                if len(Deck) <= 10:
                    Deck = deck()
                pcards = playingcards(Deck, player_cards,
                                      dealer_cards, trigger)
                # trigger=1 is used to tell so that 1 card will be given after 1st round
                trigger = 1
                # Prints player's card
                printcards(pcards, 1)
                # Gets the score of the cards per round
                playerscore = hand_value(player_cards)
                dealerscore = hand_value(dealer_cards)
                # Tells if player hit a jackblack or goes over 21
                flag = scorecheck(playerscore, round)
                lock = True

                # flag==0 indicates that player and dealer got their two cards but it is not a blackjack
                if flag == 0:
                    playerchoice()
                    roundchoice = int(input('Enter Choice: '))

                # flag==1 indicates that player hits a jackblack. It adds 10pts to the player
                elif flag == 1:
                    totalpoints += 10
                    print('You win 10 points!')
                    print('Total points: ', totalpoints)
                    contgame = continuegame()
                    # New round after getting blackjack
                    if contgame == 1:
                        player_cards.clear()
                        dealer_cards.clear()
                        round = 1
                        trigger = 0
                        lock = False
                        continue
                    # Save score to leaderboard after getting blackjack then exit
                    elif contgame == 2:
                        leaderboard = loadleaderboard()
                        name = input("Input your name: ")
                        addtoleaderboard(name, totalpoints)
                        saveleaderboard()
                        print_leaderboard(leaderboard)
                        gamestart = False
                # flag==2 indicates that player hand value exceeded 21
                elif flag == 2:
                    # Player is suggested to play again if total points is just zero
                    if totalpoints == 0:
                        print('Total points: ', totalpoints)
                        contgame = continuegame()
                        if contgame == 1:
                            print('Deck:', len(Deck))
                            player_cards.clear()
                            dealer_cards.clear()
                            round = 1
                            trigger = 0
                            lock = False
                            continue
                        elif contgame == 2:
                            gamestart = False
                    # Game ends and saves the score to leaderboard
                    elif totalpoints > 0:
                        totalpoints -= 10
                        print('Total points: ', totalpoints)
                        leaderboard = loadleaderboard()
                        name = input("Input your name: ")
                        addtoleaderboard(name, totalpoints)
                        saveleaderboard()
                        print_leaderboard(leaderboard)
                        gamestart = False

                # Player chooses to add a card to hand
                if roundchoice == 1:
                    round += 1
                    lock = False
                # Player chooses to stand. Cards on hand of player and dealer are printed
                elif roundchoice == 2:
                    printcards(pcards, 1)
                    printcards(pcards, 2)
                    print('Your score: ', playerscore)
                    print("Dealer's Score:", dealerscore, '\n')
                    # Player score and dealer score are compared
                    if playerscore > dealerscore:
                        print('You win 10 points!')
                        totalpoints += 10
                        print('Total points: ', totalpoints)
                        # Player is asked if they want to continue game
                        contgame = continuegame()
                        # Hands are cleared and other variables are reset
                        if contgame == 1:
                            player_cards.clear()
                            dealer_cards.clear()
                            round = 1
                            trigger = 0
                            lock = False
                            continue
                        # Game ends and saves the score to leaderboard
                        elif contgame == 2:
                            leaderboard = loadleaderboard()
                            name = input("Input your name: ")
                            addtoleaderboard(name, totalpoints)
                            saveleaderboard()
                            print_leaderboard(leaderboard)
                            gamestart = False
                    # Playerscore is lower than the dealer score
                    else:
                        print('You lose 10 points!')
                        # Player is suggested to play again if total points is just zero
                        if totalpoints == 0:
                            print('Total points: ', totalpoints)
                            contgame = continuegame()
                            if contgame == 1:
                                player_cards.clear()
                                dealer_cards.clear()
                                round = 1
                                trigger = 0
                                lock = False
                                continue
                            # Game ends
                            elif contgame == 2:
                                gamestart = False
                        # Game ends and saves the score to leaderboard
                        elif totalpoints > 0:
                            totalpoints -= 10
                            print('Total points: ', totalpoints)
                            leaderboard = loadleaderboard()
                            name = input("Input your name: ")
                            addtoleaderboard(name, totalpoints)
                            saveleaderboard()
                            print_leaderboard(leaderboard)
                            gamestart = False
            else:
                print('Sorry what was that?')
                break
        continue
    # Loads and prints leaderboard
    elif navigate == 2:
        leaderboard = loadleaderboard()
        print_leaderboard(leaderboard)
    # Exits game
    elif navigate == 3:
        break
    # User error
    else:
        print('Sorry, what was that?')
