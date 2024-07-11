from time import sleep
print('welcome to medium level')
ans=input('Are you ready to play(yes/no):')
user_name=input("please enter a username")
print('*************Welcome',user_name,'**************')
score=0
total_q=5
if ans.lower()=='yes':
    sleep(1)
    ans=input('1.d={0,1,2}\n for x in d:\n print(x)?\n a.{0,1,2}{0,1,2}{0,1,2}\n b.0 1 2\n c.syntax_error\nd.none of these above\n')
    if ans.lower()=='b':
        score+=1
        print('correct')
    else:
        print('incorrect. Correct answer is b.0 1 2 \n')
    sleep(1)
    ans=input('2.i=1:\n while true:\n  if i%3==0:\n\tbreak\n print(i)\na.1 2 3\nb.3 2 1\nc.1 2\nd.invalid syntax\n')
    if ans.lower()=='d':
        score+=1
        print('correct')
    else:
        print('incorrect.The correct answer is d.invalid syntax\nExplanation:invalid syntax,because thisdeclaration(i=1:)is wrong\n')
    sleep(1)
    ans=input('3.import math \n  abs (math.sqrt(36))\n what will be the output of this code?\na.error\nb.-6\nc.6\nd.6.0\n')
    if ans.lower()=='d':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is d.6.0\n Explanation :this function prints the square root of this value')
    sleep(1)
    ans=input('4.find value of x? \n x=0\nfor i in range(10):\n\t for j in range (-1,-10,-1):\n\t\tx+=1\n\t print(x)\na)99\nb)90\nc)100\nd)101\n')
    if ans.lower()=='c':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is b\n')
    sleep(1)
    ans=input('5.what is the output of the following?\n x=0 \n while(x<100):\n\t x+=2 \n print(x)\na.101\nb.99\nc.none of the above,this is an infinite loop\nd.100\n')
    if ans.lower()=='':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is d.100')

    sleep(1)
    print('Thankyou for playing you got', score, 'questions correct.')
sleep(1)    
Percentage=(score/total_q)*100
print("Percentage",str(Percentage)+'%')
sleep(1)
print(user_name,'your Percentage is ',Percentage)
print('Goodbye')
