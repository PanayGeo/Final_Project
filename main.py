import time, random
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
            user_choice=input('Choose either {Rock}, {Paper}, or {Scissors}\n')
            print('\n')
            choice_list = ['rock','paper','scissors']
            cpu_choice = random.choice(choice_list)
            user_draw = f'You cast {user_choice}'
            cpu_draw = f'Computer cast {cpu_choice}'
            cpu_value = int(choice_list.index(cpu_choice))+1
            if 'rock' in user_choice.lower():
                user_value = 1
                break
            elif 'paper' in user_choice.lower():
                user_value = 2
                break
            elif 'scissors' in user_choice.lower():
                user_value = 3   
                break
            else:
                raise ValueError
        except ValueError:
            print('that is not a valid input')
            pass      
    for item in choice_list:
        print(item.title())
        time.sleep(1)
    print(user_draw)  
    print(cpu_draw)
    if cpu_value>user_value:
        print('You Lost D:')
    elif user_value>cpu_value:
        print('You WIN!!!')
    elif user_value==cpu_value:
        print('Tie Game')
    else: 
        print('If the code broke I\'m not even suprised\n I have no idea what\'s going on anymore')
    time.sleep(x)
    wish=input('Would you like to play again? (y)es/(n)o\n')
    if 'y' in wish.lower():
        pass
    elif 'n' in wish.lower():
        break
    else:
        print('*knocks you out*')
        pass        
