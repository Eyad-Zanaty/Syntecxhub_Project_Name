import random # importing random module to generate random numbers


def guessing_hint():
    '''This function is a number guessing game where the user can choose the difficulty level (low, mid, high)'''
    
    guess= 0
    end= 0
    
    replayGuessing= True
    
    lowestAttempts= []
    
    while replayGuessing: # main loop that continues until the user decides to stop replaying
    
        while True:
            
            difficulty= input("Your guess difficulty(low/mid/high): ") # asking the user to choose the difficulty level
            difficulty.strip().lower()
            
            if difficulty == 'low':
                guess= random.randint(1, 50)
                end= 50
                break
            
            elif difficulty == 'mid':
                guess= random.randint(1, 100)
                end= 100
                break
                
            elif difficulty == 'high':
                guess= random.randint(1, 1000)
                end= 1000
                break
            
            else: 
                continue
        
        answer= 0
        attempt= 0
        
        while answer != guess: # guessing loop that continues until the user guesses the correct number
            
            try:
                answer= int(input(f"Guess a number betweem 0 to {end}: ")) # asking the user to guess a number and making sure it's an integer
            except ValueError:
                print("invalid")
                continue
            attempt+= 1
            
            if answer > end or answer < 0:
                print("invalid")
                continue
            
            elif answer > guess:
                print(f'higher hint (attempt={attempt})')
            
            elif answer < guess:
                print(f'lower hint (attempt={attempt})')
            
        
        else:
            lowestAttempts.append(attempt)
            print(f'''You got it!!
your best lowes Attempts= {min(lowestAttempts)}
''')

            
            replaying= True
            
            while replaying: # loop that continues until the user decides to replay or not
                replay= input("Do you want to replay(yes/no): ")
                replay.strip().lower()
                
                if replay == 'yes':
                    replayGuessing= True
                    replaying= False
                    
                elif replay == 'no':
                    replayGuessing= False
                    replaying= True
                    break

                else:
                    print("invalid")
                    replaying= True
                    continue
    else:
        return 0
                
        

guessing_hint()