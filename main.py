














import time, random #this starts on line 16 for good luck, idk ask ethan

# The desire to play, to game, to fire in the hole
desire = True
#while loop for the entire program
while desire == True:
    print('Hello Welcome to Roshambo')
    time.sleep(1)
    print('Otherwise known as Rock, Paper, Scissors')
    time.sleep(1)
    print('Let\'s start, shall we?\n')
    time.sleep(3)


    while True:
        #tryexcept
        try:
            user_choice=input('Choose either {Rock}, {Paper}, {Scissors} or type in a number for a random choice\n')
            print('\n')

            choice_list = ['rock','paper','scissors']
            #Library random used for computer choice
            cpu_choice = random.choice(choice_list)
            
            #do you even need to play?          answer: no
            #cast
            if int(user_choice)>0:
                user_choice=random.choice(choice_list)

            user_draw = f'You cast {user_choice}'
            cpu_draw = f'Computer cast {cpu_choice}'
            cpu_value = choice_list.index(cpu_choice)+1
                
            #ifelse 's to interpret user response
            #Method .lower just to account for odd spelling and capitalization but still be able to move forward if the input
            #is still right to a value that could be expected by the program
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
                    print("/` - T -ス")
                    time.sleep(1.3)
            else:
                raise ValueError
        except ValueError:
            print('that is not a valid input') 

    #for loop for the iconic shouting of rock paper scissors
    for item in choice_list:
        print(item.title())
        time.sleep(1)
        
    print('\n')
    time.sleep(1)
    print(user_draw.title())
    time.sleep(1)
    print(cpu_draw.title())
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



    time.sleep(3)


    wish = input('Would you like to play again? (y)es/(n)o\n')
    if 'y' in wish.lower():
        print('\n')
    elif 'simon' in wish.lower():
        print('This case just stands more as a way for me to communicate with you')
        time.sleep(4)
        print('I am genuinely sad that I won\'t have your class or you as a teacher next term')
        time.sleep(4)
        print('I know the other students in pd. 5 give you crepe for being a little kooky but that\'s why I liked your class')
        time.sleep(6)
        print('Although I did go in there knowing most stuff I still enjoyed the ways that you taught \nand that you weren\'t afraid to joke around with your students every once in a while')
        time.sleep(8)
        print('I had a very fun time in your class, actually using this knowledge I have rather then it rotting up there until I feel like doing something')
        time.sleep(4)
        print('Thank you for everything\nIt would definitely be hard forgetting about you')
        time.sleep(4)
        print('enjoy the rest of the school year\n/` - T -ス')
        time.sleep(7)
        print('imeaniknowim goingtohaveyouforcomputerscienceclub,butlikedon\'t invalidatethe messageimtryingtosay')
        time.sleep(20)
        break
    elif 'n' in wish.lower():
        break
    elif ':3' in wish:
        print('Meow')
        for i in range(20):
            print("/` - T -ス")
            time.sleep(1)
    else:
        print('*knocks you out*\n')
