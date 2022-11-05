from distutils.debug import DEBUG
from distutils.log import debug
import random
l = ["Rock","rock","Paper","paper","Scissor","scissor"]
dic = {
    "Rock": 1,
    "rock":1,
    "Paper": 2,
    "paper": 2,
    "Scissor": 3,
    "scissor":3,
    "scissor":3
    
}
userScore = 0
compScore = 0
while True:
    
    print('''
    Rock, Paper and Scissor Game start: 
            Press 1: to play the game
            Press 2: to exit the game
''')
    

    userInput = int(input("Enter Your wish: "))
    if userInput == 1:
        for ind in range(1,6):
            compChoice = random.choice(l)
            userChoice = str(input("Enter your Choice: "))
            print("""
            Computer Choice: {0}
            Your Choice: {1}
            """.format(compChoice, userChoice)
            )
            if compChoice == "Rock" or compChoice == "rock" and userChoice == "Paper" or userChoice == "paper" :
                userScore = userScore + 1
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )
            elif compChoice == "Paper" or compChoice == "paper" and userChoice == "Scissor" or userChoice == "scissor":
                userScore = userScore + 1
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )

            elif compChoice == "Scissor" or compChoice == "scissor" and userChoice == "Rock" or userChoice == "rock":
                userScore = userScore + 1
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )

            elif userChoice == "Rock" or userChoice == "rock" and compChoice == "Paper" or compChoice == "paper":
                compScore = compScore + 1
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )
                    
            elif userChoice == "Paper" or userChoice == "paper" and compChoice == "Scissor" or compChoice == "scissor":
                compScore = compScore + 1
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )

            elif userChoice == "Scissor" or userChoice == "scissor" and compChoice == "Rock" or compChoice == "rock":
                compScore = compScore + 1
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )

            elif compChoice == 'Rock' or compChoice == 'rock' and userChoice == 'Rock' or userChoice == 'rock':
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )
            elif compChoice == 'Paper' or compChoice == 'paper' and userChoice == 'Paper' or userChoice == 'paper':
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )
            elif compChoice == 'Scissor' or compChoice == 'scissor' and userChoice == 'Scissor' or userChoice == 'scissor':
                print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
            )
                    
            else:
                print("Invalid Choice...")

            
    elif userInput == 2:
        break
    else :
        print("Invalid wish...")   
        print("Please enter a valid wish...")

    if compScore > userScore:
        print("Computer Won...")
        print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
    )
    elif compScore < userScore:
        print("You Won...")
        print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
    )
    else :
        print("Match Draw...")
        print('''
    Computer Score: {0}
    Your Score: {1}
    '''.format(compScore,userScore)
    )


    


