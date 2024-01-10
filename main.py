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
            cpu_choice=random.choice(['rock','paper','scissors'])
            user_draw = f'You cast {user_choice}'
            cpu_draw = f'Computer cast {cpu_choice}'
            cpu_value = cpu_choice.index
            if 'rock' in user_choice.lower
                user_value = 1
            elif 'paper' in user_choice.lower
                user_value = 2
            elif 'scissors' in user_choice.lower
                user_value = 3   
            if 
                break      
            elif 
        except ValueError:
            print('that is not a valid input')
            pass         
    time.sleep(x)
    wish=input('Would you like to play again? (y)es/(n)o\n')
    if 'y' in wish.lower():
        pass
    elif 'n' in wish.lower():
        break
    else:
        print('*knocks you out*')
        pass        
