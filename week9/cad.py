'''from random import randint
def headortails(guess):
    value=randint(0,1)
    print (value)
    if guess==value:
        return True
    else:
        return False
guess=int(input("Enter 1 for heads and 0 for tails"))
result=headortails(guess)
if result== True:
    print ("COrrect")
else: 
    print ("worng")

    
from random import randint
def oddoreven(guess):
    value=randint(0,9)
    print(f"The value={value}")
    if value%2==0:
        answer="even"
    else:
        answer="odd"
    if answer==guess.lower():
        return True
    else:
        return False
guess=input("enter odd or even")
result=oddoreven(guess)
if result==True:
    print("correct")
else:
    print("incorrect")
    

def dup_copy(num1=0, num2=0, num3=0):
    if num1==num2 and num2==num3:
        return 3
    elif num1==num2 or num1==num3 or num2==num3:
        return 2
    else:
        return 0
num1=int(input("Enter number"))
num2=int(input("Enter 1 for heads and 0 for tails"))
num3=int(input("Enter 1 for heads and 0 for tails"))
print ("Numberj of copies:",dup_copy(num1,num2, num3))


def rockpap(player1='rock', player2='rock'):
    rules={'rock':'scissor','scissor':'papper','paper':'rock' }
    if player1==player2:
        return "tie"
    elif rules[player1]==player2:
        return "player1 wins"
    else:
        return "Player2 wins"
def game():
    p1=input("player1")
    p2=input("Player2")
    result=rockpap(p1,p2)
    return result
print(game())


def  family(name=''):
    tree={'Darth Vadar':'Father','R2D2':'Droid','Han':'Brother','Leia':'Sister'}
    if name in tree:
        return tree[name]
    else:
        return ("unknown")
def fam():
    name=input("Enter the name")
    result=family(name)
    return result
print(fam())


def ascending_order(num1, num2=5, num3=25):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1
    return [num1, num2, num3]

num1= int(input ("enter the num"))
num2= int(input ("enter the num"))
num3= int(input ("enter the num"))
print ("The ascending order is", ascending_order(num1, num2, num3))
'''
def get_indicecs(lyst, num=0):
    new=[]
    for i in range (0, len(lyst)):
        if lyst[i]==num:
            new.append(i)
    return new
lyst=list(map(int, input("Enter numbers separated by spaces").split()))
num=(input("enter number or enter for defailt 0"))
if num=="":
    result= get_indicecs(lyst)
else:
    result=get_indicecs(lyst, int(num))

print("indices", result)


    
