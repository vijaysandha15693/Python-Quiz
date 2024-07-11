from time import sleep
print('welcome to difficult level')
ans=input('Are you ready to play(yes/no):')
user_name=input("please enter a username")
print('*************Welcome',user_name,'**************')
score=0
total_q=5
if ans.lower()=='yes':
    sleep(1)
    ans=input('1.Which of the following is a Python tuple?\n a.[1, 2, 3]\n b.(1, 2, 3)\n c.{1, 2, 3}\n d.{}\n')
    if ans.lower()=='b':
        score+=1
        print('correct')
    else:
        print('incorrect. Correct answer is b.(1, 2, 3)\nExplanation: Tuples are represented with round brackets.\n')
    sleep(1)
    ans=input('2.What will be the output of the following Python code?\n>>>t1 = (1, 2, 4, 3)\n>>>t2 = (1, 2, 3, 4)\n>>>t1 < t2\n\na.True\nb.False\nc.Error\nd.None\n')
    if ans.lower()=='b':
        score+=1
        print('correct')
    else:
        print('incorrect.The correct answer is b.False\nExplanation: Elements are compared one by one in this case.\n')
    sleep(1)
    ans=input('3.To remove string “hello” from list1, we use which command?\na.list1.remove(“hello”)\nb. list1.remove(hello)\nc. list1.removeAll(“hello”)\nd) list1.removeOne(“hello”)\n')
    if ans.lower()=='a':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is a.list1.remove(“hello”)\n')
    sleep(1)
    ans=input('4.What will be the output of the following Python code snippet?\n>>> a={1:"A",2:"B",3:"C"}\n>>> del a\na) method del doesn’t exist for the dictionary\nb) del deletes the values in the dictionary\nc) del deletes the entire dictionary\nd) del deletes the keys in the dictionary\n')
    if ans.lower()=='c':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is c\nExplanation: del deletes the entire dictionary and any further attempt to access it will throw an error.\n')
    sleep(1)
    ans=input('5. Which of the following command is used to open a file “c:\temp.txt” in read-mode only?\na. infile = open(“c:\temp.txt”, “r”)\nb. infile = open(“c:\\temp.txt”, “r”)\nc. infile = open(file = “c:\temp.txt”, “r+”)\nd. infile = open(file = “c:\\temp.txt”, “r+”)\n')
    if ans.lower()=='':
        score+=1
        print('correct')
    else:
        print('incorrect. The correct answer is b.infile = open(“c:\\temp.txt”, “r”)')
    sleep(1)

    print('Thankyou for playing you got', score, 'questions correct.')
sleep(1)    
Percentage=(score/total_q)*100
print("Percentage",str(Percentage)+'%')
print(user_name,'your Percentage is ',Percentage)
sleep(1)
print('Goodbye')
