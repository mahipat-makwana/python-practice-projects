import random

#create a bag with 10 marbles
bag = ('green','green','green','green','green','black','red','red','red','white')

#starting amount of money
start_purse = 1000
# current money amount
purse = start_purse
#result of last round
result = 0
#how many rounds
rounds = 3
#last marble
marble = 'none'
# welcome user to game
print(f'You start the game with {start_purse} gold coins')

#Define Custom Exceptions
class ValueLowerError(Exception):
    pass
class ValueHigherError(Exception):
    pass

# loop drawing marbles
for draw in range(1, rounds+1):
    #how much was bet
    try:
        bet = int(input(f"Current Purse: {purse} | Last draw: {marble} \nRound {draw} - How much do you want to bet?: "))
        if bet > purse:
            raise ValueHigherError("Insufficient Amount")
        if bet < 0:
            raise ValueLowerError("Invalid Amount")
    except ValueError:
        print(f'Invalid input')
        break
    except ValueHigherError:
        print(f'Insufficient Amount, Current Purse: {purse}')
        break
    except ValueLowerError:
        print(f'Invalid Input Amount {bet}')
        break
    else:
    #draw marble
        marble = random.choice(bag)
# win or loss
        if marble == 'green':
            result = bet
        elif marble == 'black':
            result = 10*bet
        elif marble == 'white':
            result = -5*bet
        else:
            result = -bet
#calc win or loss/ result and new amount/purse
        purse += result
#lose game if lose half of money
        if purse < 0.5*start_purse:
            print(f'Game over! You lost too much gold!!!')
            break
#print results
        print(f'Purse: {purse}, last result: ({marble}): {result}')
        print('')
# print final results
print(f'Starting: {start_purse} / Ending: {purse}')
print(f'Gain/Loss {round(((purse-start_purse)/start_purse),2) * 100}%')


