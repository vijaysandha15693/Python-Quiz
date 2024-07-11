from time import sleep
print('welcome to easy level')
ans=input('Are you ready to play(yes/no):')
user_name=input("please enter a username")
print('*************Welcome',user_name,'**************')
score=0
total_q=5
if ans.lower()=='yes':
    ans=input("""1.Python was developed in which year?
A. 1972
B. 1995
C. 1989
D. 1981\n""")
    if ans.lower()=='c':
        score+=1
        print('correct')
    else:
        print('incorrect. Correct answer is c. 1989\n Explanation: Python was introduced by Guido Van Rossum in 1989.\n')
    sleep(1)
    ans=input(""""2. What is the extension of python file?
A. .p
B. .py
C. .python
D. None of the above \n""")
    if ans.lower()=='b':
        score+=1
        print('correct')
    else:
        print('incorrect.The correct answer is b. .py \nExplanation:  Python file is saved with an extension .py.\n')
    sleep(1)
    ans=input("""3. What is output for − 2 * 2 **3
A - 12
B - 64
C - 16
D - 26 \n""")
    if ans.lower()=='c':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is c. 16 2*3 gives 2*2*2 i.e. 8, then 2*8 gives 16, since order of precedence is * then*. ** implies ‘‘ raise to power\n')
    sleep(1)
    ans=input("""4. What is the output for - 'you are doing well' [2:999]
A - 'you are doing well'
B - ' '
C - Index error
D - u are doing well.\n""")
    if ans.lower()=='d':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is d. \nExplanation: Slicing will never give us an error even if we give it too large of an index for the string. It will just return the widest matching slice it can.\n')
    sleep(1)
    ans=input("""5.Which one of the following has the highest precedence in the expression?
a) Exponential
b) Addition
c) Multiplication
d) Parentheses\n""")
    if ans.lower()=='d':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is d.\nExplanation:  Just remember: PEMDAS, that is, Parenthesis, Exponentiation, Division, Multiplication, Addition, Subtraction.')
        print('Thankyou for playing you got', score, 'questions correct.')
    sleep(1)
    Percentage=((score/total_q)*100)
    print('Percentage:', str(Percentage)+'%')
print(user_name,'your Percentage is ',Percentage)
sleep(1)
print('Goodbye')
