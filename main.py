














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
            user_choice=input('Choose either {Rock}, {Paper}, {Scissors} or type f for a random choice\n').lower()
            choice_list = ['rock','paper','scissors']
            assert(user_choice in choice_list)
            print('\n')
            break
        except AssertionError:
            if user_choice == 'f':
                user_choice = random_user_choice
                user_value = choice_list.index(user_choice)+1
                break
            else:
                print('That is not a valid choice')
                

        #Library random used for computer choice
    cpu_choice = random.choice(choice_list)
        
    #ifelifelse's to interpret user response
    #Method .lower just to account for odd spelling and capitalization but still be able to move forward if the input
    #is still right to a value that could be expected by the program
    if 'rock' in user_choice:
        user_value = 1
        break
    elif 'paper' in user_choice:
        user_value = 2
        break
    elif 'scissors' in user_choice:
        user_value = 3
        break
    elif ':3' in user_choice:
        print('Meow')
        for i in range(20):
            print("/` - T -ス")
            time.sleep(1.3)
    #do you even need to play?          answer: no
    elif 'trivia' in user_choice:
        print('Welcome to easter egg trivia!!!!')
        time.sleep(1)
        print('🎉🎉🎉')
        time.sleep(1)
        print('You shouldn\'t be here')
        time.sleep(1)
        print("BUT SINCE YOU ARE LET'S PLAY SOME TRIVIA")
        score=0
        time.sleep(2)
        #Casting
        q1=input('What is Mr. Toaha\'s first name?(Lore Accurate)\n(1.Zaccariah\n(2.Simon\n(3.Mister\n(4.Blank (No name)\n')
        if q1 == '4':
            print('YOU ARE CORRECT')
            score+=1
        elif q1 == '3':
            print('I\'ll accept it')
            score+=1
        else:
            print('WRONG!!!')
        time.sleep(1)
        print('Next question')
        time.sleep(1)
        q2=input('Are Simon and Mr. Toaha the same person?\n(1.Yes\n(2.No\n(3.Maybe\n')
        if q2 == '2':
            print('YOU ARE CORRECT')
            score+=1
        elif q2 == '3':
            print('shhhhhh')
            score+=1
        else:
            print('WRONG!!!')
        time.sleep(1)
        print('Next question')
        time.sleep(2)
        #casting it NEEDS to be a number
        q3=int(input('What is an acceptable score in the eyes of Mr. Toaha? \n(Please enter a numeric value):'))
        if q3 > 100:
            print('YOU ARE CORRECT')
            score+=1
        elif q3 == 100:
            print('it\'s')
            time.sleep(1)
            print('acceptable')
            score+=1
        else:
            print('That is borderline failing')
        time.sleep(1)
        print('Next question')
        time.sleep(2)
        q4=input("Which Toaha Brother was locked away FOR LIFE?\n(1.          Toaha\n(2.Simon Toaha\n(3.Sir Toaha\n(4.Señor Toaha\n")
        if q4 == '3':
            print('YOU ARE CORRECT')
            score+=1
        else:
            print('WRONG!!!')
        time.sleep(1)
        print('Next question')
        time.sleep(1)
        while True:
            q5=input('I\'m out of questions\n(1.Great thinking stoobid\n(2.fun while it lasted :D\n(3.@#$! *@#\n(4.Fire in the hole\n')
            if q5 == '1':
                print('Well you don\'t have to be so rude about it D:<')
                time.sleep(1)
                print('Good day SIR!')
                score-=1
                time.sleep(1)
                print('Your score was '+str(score)+' out of 5')
                break
            elif q5 == '2':
                print('it was')
                time.sleep(1)
                print('okie bye ヾ(≧▽≦*)o')
                score+=1
                time.sleep(1)
                print('Your score was '+str(score)+' out of 5')
                break
            elif q5 == '3':
                print('Well alright then')
                time.sleep(1)
                print('quite immature of you')
                score-=1
                time.sleep(1)
                print('Your score was '+str(score)+' out of 5')
                break
            elif q5 == '4':
                print('Fire in the hole 🙂')
                score+=1
                time.sleep(1)
                print('Your score was '+str(score)+' out of 5')
                break
            else:
                time.sleep(2)
                print('Well don\'t just stand there')
                time.sleep(2)
                print('\n\n\n\n\n\n\n\n')
    
    
    
    user_draw = f'You cast {user_choice}'
    cpu_draw = f'Computer cast {cpu_choice}'
    cpu_value = choice_list.index(cpu_choice)+1
    

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
