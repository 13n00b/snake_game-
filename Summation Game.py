print("Welcome and thanks for playing the game!")

playing = input("Shall we proceed with level 1 of this game? ")

if playing.lower() != ("yes"):
    quit()
print("Let's enjoy adding then :-)")

answer = input("what is the sum of 4+4? ")
if answer == '8':
    print("You are awesome! ;-)")
    print("Congratulations! You have completed Level 1 of this summation game")
    playing = input("Proceed to level 2? ")
    if playing.lower() != "yes":
        quit()
    else:
        print("Welcome to Level 2!")
        answer = input("What is 16+49? ")
        if answer == '65':
            print("Congratulations! You have completed the level 2 of this summation game")
            playing = input("Proceed to level 3? ")
            if playing.lower() != "yes":
                quit()
            else:
                print("Welcome to level 3!")
                answer = input("What is 326+255? ")
                if answer == '581':
                    print("Congratulations! You have completed level 3 of this summation game")
                    playing = input("Proceed to level 4? ")
                    if playing.lower() != 'yes':
                        quit()
                    else:
                        print("Welcome to level 4")
                        answer = input("What is 2378+8921? ")
                        if answer == '11299':
                            print("Congratulations! You have completed all the levels of this summation game")
                            print("You have proved that you are a math genius! ;-)")
                        else:
                            print("Sorry, but the answer was wrong :-(")
                            print("Why don't you try again?")
                            quit()
                else:
                    print("Sorry, but the answer was wrong :-(")
                    print("Why don't you try again?")
                    quit()
        else:
            print("Sorry, but the answer was wrong :-(")
            print("Why don't you try again?")
            quit()
else:
    print("Sorry, but the answer was wrong :-(")
    print("Why don't you try again?")
    quit()
