# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  
# A note on style: Dictionaries can be defined before or after functions.
#Dictionary
tic_tac_toe= {'TL': '', 'TM': '', 'TR': '',
            'ML': '', 'MM': '', 'MR': '',
            'BL': '', 'BM': '', 'BR': ''}
#Tic tac toe board

def make_board(tic_tac_toe):
    print(tic_tac_toe['TL'] + '|' + tic_tac_toe['TM'] + '|' + tic_tac_toe['TR'])
    print('-+-+-')
    print(tic_tac_toe['ML'] + '|' + tic_tac_toe['MM'] + '|' + tic_tac_toe['MR'])
    print('-+-+-')
    print(tic_tac_toe['BL'] + '|' + tic_tac_toe['BM'] + '|' + tic_tac_toe['BR'])

def game():

    player1 = 'X'
    player2 = 'O'
    print("Hello welcome to tic tac toe! Just before you start playing you need to know how to place X and O")
    print("For top left, type 'TL', for top middle type 'TM', for top right type 'TR'" )
    print("For middle left, type 'ML', for middle middle, type 'MM', for middle right, type 'MR'")
    print("For bottom right, type 'BR', for bottom middle type 'BM', for bottom right, type 'BR")
    
    for i in range(5):
        
        try:
            choice = input("Your turn " + player1 + " where do you want to move? ")
            if tic_tac_toe[choice] == '':
                tic_tac_toe[choice] = player1
                make_board(tic_tac_toe)
                if player1 == 'TL' and player1 == 'TM' and player1 == "TR":
                    print("Good game! Player 1 wins!")
                    break
                elif player1 == 'ML' and player1 == 'MM' and player1 == 'MR':
                    print("Good game! Player 1 wins!")
                    break
                elif player1 == 'BL' and player1 == 'BM' and player1 == 'BR':
                    print("Good game! Player 1 wins!")
                    break
                elif player1 == 'TL' and player1 == 'ML' and player1 == 'BL':
                    print("Good game! Player 1 wins!")
                    break
                elif player1 == 'TM' and player1 == 'MM' and player1 == 'BM':
                    print("Good game! Player 1 wins!")
                    break
                elif player1 == 'TR' and player1 == 'MR' and player1 == 'BR':
                    print("Good game! Player 1 wins!")
                    break
                elif player1 == 'TR' and player1 == 'MM' and player1 == 'BL':
                    print("Good game! Player 1 wins!")
                    break
                elif player1 == 'TL' and player1 == 'MM' and player1 == 'BR':
                    print("Good game! Player 1 wins!")
                    break
            else:
                print("That spot is already filled. Try again.")
        except:
            print("Thats not a spot")

        try:
            choice = input("Your turn " + player2 + " where do you want to move? ")
            if tic_tac_toe[choice] == '':
                tic_tac_toe[choice] = player2
                make_board(tic_tac_toe)
                if player2 == 'TL' and player2 == 'TM' and player2 == "TR":
                    print("Good game! Player 2 wins!")
                    break
                elif player2 == 'ML' and player2 == 'MM' and player2 == 'MR':
                    print("Good game! Player 2 wins!")
                    break
                elif player2 == 'BL' and player2 == 'BM' and player2 == 'BR':
                    print("Good game! Player 2 wins!")
                    break
                elif player2 == 'TL' and player2 == 'ML' and player2 == 'BL':
                    print("Good game! Player 2 wins!")
                    break
                elif player2 == 'TM' and player2 == 'MM' and player2 == 'BM':
                    print("Good game! Player 2 wins!")
                    break
                elif player2 == 'TR' and player2 == 'MR' and player2 == 'BR':
                    print("Good game! Player 2 wins!")
                    break
                elif player2 == 'TR' and player2 == 'MM' and player2 == 'BL':
                    print("Good game! Player 2 wins!")
                    break
                elif player2 == 'TL' and player2 == 'MM' and player2 == 'BR':
                    print("Good game! Player 2 wins!")
                    break
            else:
                print("That spot is already filled. Try again.")
        except:
            print("Thats not a spot")
        
print("I hope you enjoyed the game. Goodbye!")

game()