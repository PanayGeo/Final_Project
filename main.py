import time, random
desire = True
while desire == True:

    wish=input('Would you like to play again? (y)es/(n)o\n')
    if 'y' in wish.lower():
        pass
    elif 'n' in wish.lower():
        break
    else:
        print('*knocks you out*')
        pass        
