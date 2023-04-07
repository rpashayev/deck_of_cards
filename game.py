from classes.deck import Deck
from classes.card import Card
from classes.player import Player

# create Deck instance
bicycle = Deck()

print('Number of players:')
isInt = False
while not isInt:
    number_of_players = input()
    if number_of_players.isdigit():
        isInt = True
        number_of_players = int(number_of_players)

# create player instances
for i in range(number_of_players):
    player_name = input(f'Player {i+1} name is: \n')
    Player(player_name)

# welcome message and rules
print(f'\nThe rule is very simple: guess the suit of the next card and if its rank to the current card.\nType "higher", "lower" or "equal" for the rank and "spades", "hearts", "clubs" or "diamonds" for suits.\nTo stop the game type "stop" on any question\n --------\nPoints:\n +5 points for suit\n +10 for rank\n +20 for both\n\nAnd here is your first card:')

# end game message
def end_game():
    for player in Player.players:
        print(f'{player.name} score is {player.points}')
        
# game cycle function
def game_cycle():
    current = bicycle.draw_card().current_card
    current.card_info()
    
    while len(bicycle.cards) > 0:
        for p in Player.players:
            print(f'{p.name} turn')
            suit_guess = input('What is the suit of the next card?: ')
            card_guess = input('Is it higher, lower or equal to current?: ')
            
            if card_guess == 'stop' or suit_guess == 'stop':
                print(f'{len(bicycle.cards)} cards left in the deck.\n')
                end_game()
                return False
            else:
                next = bicycle.draw_card().current_card
                if ((next.point_val > current.point_val and card_guess.lower() == 'higher') or (next.point_val < current.point_val and card_guess.lower() == 'lower') or (next.point_val == current.point_val and card_guess.lower() == 'equal')):
                    if suit_guess.lower() == next.suit:
                        print(f'Do you have crystal ball?!! \n +20 points')
                        p.increase_points(2)
                    else:
                        print(f'Nice try! \n +10 points')
                        p.increase_points(1)
                elif suit_guess.lower() == next.suit:
                    print(f'Good, but you can do better!! \n +5 points')
                    p.increase_points(0.5)
                else:
                    print('Nope... :(')
                    
                print(f'\nDrawn card is')
                next.card_info()
                
                current = next
    else:
        print(f'That was the last card!')
        end_game()

game_cycle()
