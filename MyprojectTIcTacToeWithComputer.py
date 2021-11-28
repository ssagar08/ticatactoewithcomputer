import random as ra
a={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

def printboad(uboard):
    print(uboard['7']+'|'+uboard['8']+'|'+uboard['9'])
    print('-+-+-')
    print(uboard['4'] + '|' + uboard['5'] + '|' + uboard['6'])
    print('-+-+-')
    print(uboard['1'] + '|' + uboard['2'] + '|' + uboard['3'])

def validinput():
    try:
        print("Who wants to go first press 1 for you and press 0 for computer")
        game_round= int(input())
    except ValueError:
        print('Enter correct response')
        return validinput()
    if (game_round==0 or game_round==1):
        return game_round

    else:
        print('Enter valid input')
        return validinput()

def tictac():
    chance='X'
    count=0
    first_chance = validinput()

    if (first_chance == 1):
        print('You are going first')
    else:
        print(' Oh you are giving chance to computer to go first')

    computer_round=['1','2','3','4','5','6','7','8','9']
    print("THe game starts")


    for i in range(10):
        print('**************************')

        printboad(a)
        print('******************************')

        if(first_chance==1):
            print('Where do you want to go next')
            position = input()
            if a[position] == ' ':
                a[position] = chance
                count += 1
                first_chance=0
                print('You went for position {0}'.format(position))
                print()
                if chance == 'X':
                    chance = 'O'
                else:
                    chance = 'X'
            else:
                print('Positon already exists')
                print()
                print(' Where do you wnat to go ')
        else:
            computer_position= ra.choice(computer_round)
            print()
            print('Computer choses to go for  {0}'.format(computer_position))
            print()
            if a[computer_position] == ' ':
                a[computer_position] = chance
                count += 1
                first_chance = 1
                print()
                print('Computer Goes at {0}'.format(computer_position))
                print()

                if chance == 'X':
                    chance = 'O'
                else:
                    chance = 'X'

            else:
                print('Positon already exists')
                print()
                print(' Where do you wnat to go ')
                print()





        if(count>=5):
            if a['4'] == a['5'] == a['6'] != ' ':
                printboad(a)
                print("Congratullations" + chance + 'loses')
                break
            if a['1'] == a['2'] == a['3'] != ' ':
                printboad(a)
                print("Congratullations" + chance + 'loses')
                break
            if a['7'] == a['4'] == a['1'] != ' ':
                printboad(a)
                print("Congratullations" + chance + 'loses')
                break
            if a['8'] == a['5'] == a['2'] != ' ':
                printboad(a)
                print("Congratullations" + chance + 'loses')
                break
            if a['9'] == a['6'] == a['3'] != ' ':
                print_board(a)
                print("Congratullations" + chance + 'loses')
                break
            if a['7'] == a['5'] == a['3'] != ' ':
                printboad(a)
                print("Congratullations" + chance + 'loses')
                break
            if a['1'] == a['5'] == a['9'] != ' ':
                printboad(a)
                print("Congratullations\t\t" + chance + 'loses')
                break

        if count == 9:
            print('Game tied')

tictac()





