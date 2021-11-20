from time import sleep
from random import choice

player_score, bot_score = 0, 0      #* Inititalize scores

def start_main():       #* Interface menu
    print('\n-----------------------------------')
    print("|WELCOME TO ROCK, PAPER, SCISSORS |")
    print("-----------------------------------")
    print('|1. Rules                         |')
    print('|2. Play                          |')
    print('|3. Exit                          |')
    print('|4. About                         |')
    print("-----------------------------------\n")
    
    choice = int(input('Enter your choice: '))
    
    print('\n');sleep(1)

    if choice == 1:choice1()    #* Choice 1 - Rules
    
    elif choice == 2:Bot()
    
    elif choice == 3:choice3()
    
    elif choice == 4:choice4()
    
    else:print('WRONG CHOICE');start_main()    #* Wrong input by the user

def choice1():          #* Defining the rules for the game in the function

    print('1. Use your keyboard keys to enter your choice. \n 1(a) R/r-Rock \n 1(b) S/s-Scissors \n 1(c) P/p - Paper\n')
    sleep(4)
    
    print('2. Rock defeats scissors, scissors defeats paper and paper defeats rock.\n')
    sleep(3)
    
    ask = input('Ready to play? [Y/N]')      #* Ask the user if they are ready to play
    
    print('\n')
    
    if ask in ('y', 'Y'):Bot()     #* User is ready to play
    
    elif ask in('n', 'N'):         #* User is not ready to play
        sleep(1)
        print('Exiting to main menu.....\n')
        sleep(1)
        start_main()
    
    else:print('Wrong Choice')     #* Wrong choice entered by the user


def choice3():print('Exiting....\n');sleep(1)   #*Function for choice 3 (To exit the game)


def choice4():          #* Printing the about screen
    print('\n-------------------------')
    print('|Made By:- Jai Verma :D |')
    print('-------------------------\n')
    sleep(5)
    start_main()

def Bot():      #* The game start Function

    def start():        #* Input the no of rounds the user wants to play

        global rounds, i
        
        rounds = int(input('Enter no of Rounds[Max 100]: '))
        
        if rounds in range(1, 101):     #* Check if the user enetered the correct no of rounds
            for i in range(0, rounds):  
                i += 1
                play_user()             #* User plays the no of times they entered
        
        else:                           #* Wrong input provided by the user
            print('\nInvalid!!\n')
            start()                     #* Asks the no. of rounds again
        
        scores()                        #* After the end of the game, displaying the score


    def scores():               #* Score function to provide scores
        
        print('----------------------')
        print('|Final Scores are:   |')
        print('----------------------')
        print(f'|Player Score = {player_score}    |')
        print(f'|Bot Score = {bot_score}       |')
        print('----------------------')
        
        if player_score > bot_score:      #* Player wins the game
            print('|Result: You Won     |');print('----------------------')
        
        elif player_score == bot_score:   #* both have equal scores
            print('|Result: Its a Tie   |');print('----------------------')
        
        else:                             #* The bot wins the game
            print('|Result: The bot Won |');print('----------------------\n')

    
    def play_user():       #* User's turn in the round  

        print(i, 'round\n')    #* Prints the number of rounds the user is on
        
        player_choose = input('What do you choose? [Rock(r)/paper(p)/scissors(s)] >>')  #* Choosing an option
        
        if player_choose in ('r', 'R'):     #* Player chooses rock
            player_choose_rock()            #* Head to this function
        
        elif player_choose in ('S', 's'):   #* Player chooses scissors
            player_choose_scissors()        #* Head to this function
        
        elif player_choose in ('p', 'P'):   #* Player chooses paper
            player_choose_paper()           #* Head to this function
        
        else:        #* Wrong choice 
            print('\nWrong Choice!');play_user()
            
    
    def play_bot():            #* Find the bots choice
        global bot_choice
        
        choices = ['Rock', 'Paper', 'Scissors']
        
        bot_choice = choice(choices)

    
    def player_choose_rock():   #* function when player chooses rock
        
        global player_score, bot_score
        
        print('You chose Rock!');sleep(1)
        print("Let's see what the bot chooses....");sleep(1)
        
        play_bot()          #* Get the bots choice from this function
        
        print('The Bot chose', bot_choice,'.\n');sleep(1)    #* Show the bots choice
        
        if bot_choice == 'Scissors':        #* Compare the choices and increment the score of the winner
            print('You Won!!\n')
            player_score += 1       
        
        elif bot_choice == 'Paper':
            print('The Bot Won this round.\n')
            bot_score += 1
        
        elif bot_choice == 'Rock':
            print('Its a Tie.\n')
            
        
    def player_choose_scissors():       #* function Called when player chose scissors

        global player_score, bot_score
        
        print('You chose Scissors!');sleep(1)
        print("Let's see what the bot chooses....");sleep(1)
        
        play_bot();sleep(1)     #* get the bots choice
        
        print('The Bot chose', bot_choice, '.\n');sleep(1)      #* Display the bots choice
        
        if bot_choice == 'Scissors': #* Compare the results and increment scores of the winner
            print('Its a Tie.\n')             
        
        elif bot_choice == 'Paper':
            print('You Won!!\n')
            player_score += 1
            
        elif bot_choice == 'Rock':
            print('The Bot Won this round.\n')
            bot_score += 1
            
        
    def player_choose_paper():       #* function Called when player chose paper

        global player_score, bot_score
        
        print('You chose Paper!');sleep(1)
        print("Let's see what the bot chooses....");sleep(2)
        
        play_bot();sleep(1)         #* get the bots choice
        
        print('The Bot chose', bot_choice, '.\n');sleep(1)       #* Display the bots choice
        
        if bot_choice == 'Scissors':  #* Compare the results and increment scores of the winner
            print('The Bot Won this round.\n')
            bot_score += 1           
        
        elif bot_choice == 'Paper':
            print('Its a Tie.\n')   
        
        elif bot_choice == 'Rock':
            print('You Won!!\n')
            player_score += 1
    
    start()         #* Start the rounds input function

start_main()  #* Start the main program