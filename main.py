elif 'trivia' in user_choice:
                print('Welcome to easter egg trivia!!!!')
                time.sleep(1)
                print('🎉🎉🎉')
                time.sleep(1)
                print('You shouldn\'t be here')
                time.sleep(1)
                print("BUT SINCE YOU ARE LET'S PLAY SOME TRIVIA")
                score=0
                
                #casting
                q1=int(input('What is Mr. Toaha\'s first name?(Lore Accurate)\n(1.Zaccariah\n(2.Simon\n(3.Mister\n(4.Blank (No name)\n'))
                if q1 == 4:
                    print('YOU ARE CORRECT')
                    score+=1
                elif q1 == 3:
                    print('I\'ll accept it')
                    score+=1
                else:
                    print('WRONG!!!')

                print('Next question')

                q2=int(input('Are Simon and Mr. Toaha the same person?\n(1.Yes\n(2.No\n(3.Maybe\n'))
                if q2 == 2:
                    print('YOU ARE CORRECT')
                    score+=1
                elif q2 == 3:
                    print('shhhhhh')
                    score+=1
                else:
                    print('WRONG!!!')

                print('Next question')

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

                print('Next question')

                q4=int(input("Which Toaha Brother was locked away FOR LIFE?\n(1.          Toaha\n(2.Simon Toaha\n(3.Sir Toaha\n(4.Señor Toaha\n"))
                if q4 == 3:
                    print('YOU ARE CORRECT')
                    score+=1
                else:
                    print('WRONG!!!')

                print('Next question')
                while True:
                    q5=int(input('I\'m out of questions\n(1.Great thinking stoobid\n(2.fun while it lasted :D\n(3.@#$! *@#\n(4.Fire in the hole\n)'))
                    if q5 == 1:
                        print('Well you don\'t have to be so rude about it D:<')
                        time.sleep(1)
                        print('Good day SIR!')
                        break
                    elif q5 == 2:
                        print('it was')
                        time.sleep(1)
                        print('okie bye ヾ(≧▽≦*)o')
                        break
                    elif q5 == 3:
                        print('Well alright then')
                        time.sleep(1)
                        print('quite immature of you')
                        break
                    elif q5 == 4:
                        print('Fire in the hole 🙂')
                        break
                    else:
                        time.sleep(1)
                        print('Well don\'t just stand there')
