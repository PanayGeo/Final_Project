import time, random
desire = True
while desire == True:
    print('Hello Welcome to Roshambo')
    time.sleep(1)
    print('otherwose known as Rock, Paper, Sciccors')
    time.sleep(3)
    wish=input('Would you like to play again? (y)es/(n)o\n')
    if 'y' in wish.lower():
        pass
    elif 'n' in wish.lower():
        break
    else:
        print('*knocks you out*')
        pass        
