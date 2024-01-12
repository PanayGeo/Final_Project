














import time, random

# The desire to play, to game, to fire in the hole
desire = True
while desire == True:
    x=1
    print('Hello Welcome to Roshambo')
    time.sleep(x)
    print('Otherwise known as Rock, Paper, Sciccors')
    time.sleep(x)
    print('Let\'s start, shall we?\n')
    x=3
    time.sleep(x)


    while True:
        try:
            x=1
            user_choice=input('Choose either {Rock}, {Paper}, {Scissors} or type G for a random choice\n')
            print('\n')

            choice_list = ['rock','paper','scissors']
            cpu_choice = random.choice(choice_list)

            user_draw = f'You cast {user_choice}'
            cpu_draw = f'Computer cast {cpu_choice}'

            cpu_value = int(choice_list.index(cpu_choice))+1
            
            #do you even need to play?
            if 'g' in user_choice.lower():
                user_choice=random.choice(choice_list)

            if 'rock' in user_choice.lower():
                user_value = 1
                break
            elif 'paper' in user_choice.lower():
                user_value = 2
                break
            elif 'scissors' in user_choice.lower():
                user_value = 3   
                break
            elif ':3' in user_choice:
                print('Meow')
                for i in range(20):
                    print("/` - T -\.")
                    time.sleep(1)
            else:
                raise ValueError
        except ValueError:
            print('that is not a valid input') 

    for item in choice_list:
        print(item.title())
        time.sleep(1)

    time.sleep(1)
    print(user_draw)
    time.sleep(1)
    print(cpu_draw)
    time.sleep(1)

    if user_value==cpu_value:
        print('Tie Game')

    #rock scissors cases 
    elif cpu_value>user_value or user_value>cpu_value:
        if cpu_value == 3 and user_value == 1:
            print('You WIN!!!')
        elif user_value == 3 and cpu_value == 1:
            print('You Lost D:')
    #scissors beats paper, paper beats rock        
        elif cpu_value>user_value:
            print('You Lost D:')
        elif user_value>cpu_value:
            print('You WIN!!!')
        else: 
            print('If the code broke I\'m not even suprised\n I have no idea what\'s going on anymore')



    time.sleep(x)


    wish = input('Would you like to play again? (y)es/(n)o\n')
    if 'y' in wish.lower():
        print('\n')
    elif 'n' in wish.lower():
        break
    else:
        print('*knocks you out*\n')
