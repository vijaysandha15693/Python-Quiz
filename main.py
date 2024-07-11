from time import sleep
def EASY():
    EASY()
def MEDIUM():
    MEDIUM()
def DIFFICULT():
    DIFFICULT()
def rules():
    rules()
def about():
    about()
def review():
    review()
if __name__ == "__main__":
    choice = 1
    while choice != 7:
        print('\n=========WELCOME TO QUIZ MASTER==========')
        print('-----------------------------------------')
        import datetime
        now = datetime.datetime.now()
        print("current date and time is:")
        print(now.strftime("%y-%m-%d %H:%M:%S"))
        sleep(2)
        print('1. PLAY easy level')
        print('2. PLAY MEDIUM LEVEL')
        print('3. PLAY DIFFICULT LEVEL')
        print('4 SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
        print('5. ABOUT US')
        print('6.Review')
        print('7. EXIT')
        choice = int(input('ENTER YOUR CHOICE: '))
        if choice == 1:
            import easy
        elif choice == 2:
            import medium
        elif choice == 3:
            import difficult
        elif choice == 4:
            import rules
        elif choice == 5:
            import aboutus
        elif choice == 6:
            import review
        elif choice == 7:
            break
        else:
            print('WRONG INPUT. ENTER THE CHOICE AGAIN')
