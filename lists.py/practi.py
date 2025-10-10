''''
def largest_even(numbers):
    largest = -1
    for n in numbers:
        if n % 2 == 0 and n > largest:
            largest = n
    return largest

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(largest_even(nums))


def factors_int(num):
    factors=[]
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors
num= int(input("enter a number"))
print("Your factors of the numbers are:", factors_int(num))



def sum_of(num):
    even_num=0
    odd_num=0
    for i in num:
        if i % 2 == 0:
            even_num+=i
        else:
            odd_num+=i
    if even_num>odd_num:
        return "Even"
    else:
        return "Odd"
num=(list(map(int, input ("enter integers in separated spaces").split())))
print("The winner is:", sum_of(num))


def run_lists(list1, list2):
    result=[]
    for i in range(len(list1)):
        result.append(list1[i]+list2[i])
    return result
list1=list(map(int,input("enter numbers in separated soaces").split()))
list2=list(map(int,input("enter numbers in separated soaces").split()))
print(run_lists(list1, list2))


def largest_among(num):
    largest=-1
    for i in num:
        if i % 2==0 and i>largest:
            largest= i
    return largest
num=list(map(int, input ("enter numbers").split()))
print (largest_among(num))


def count_days(days):
    count=0
    for i in range(1, len(days)):
        if days[i]>days[i-1]:
            count+=1
    return count
days=list(map(int, input ("enter the miles").split()))
print (count_days(days))



def lag_days(miles):
    count=0
    for i in range(1, len(miles)):
        if miles[i]<miles[i-1]:
            count+=1 
    return count
miles=list(map(int, input("enter miles").split()))
print("The lag days are:",lag_days(miles))


def yout_tube(events):
    state= "nothing"
    for i in events:
        if i == state:
            state="nothing"
        else:
            state= i
    return state
events= input("Enter the events(like/dislike)").split()
print (yout_tube(events))

#indices and item

def indices_item(indi, item):
    indices=0
    for i in range(len(indi)):
        if indi[i] == item:
            indices+=1
    return indices
indi=(input("Enter indices").split())
item=(input("enter item"))
print (indices_item(indi, item))


def multiples_len(num, length):
    multiple=[]
    for i in range (1, length+1):
        multiple.append(num*i)
    return multiple
num=int(input("enter a number"))
length=int(input("Enter the length of the multipile"))
print(multiples_len(num, length))


def black_jack(cards):
    total=0
    for i in cards:
        if i in [2,3,4,5,6]:
            total+=1
        elif i in [7,8,9]:
            total+=0
        else:
            total+=-1
    return total
cards_input=input("enter the cards in number of letter(j,k)").split()
cards=[]
for c in cards_input:
    if c.isdigit():
        cards.append(int(c))
    else:
        cards.append(c.lower())
print(black_jack(cards))


def acronym_words(s, words):
    if len(s)!=len(words):
        return False
    acronym=""
    for i in words:
        if len(i)== 0:
            return False
        acronym+=i[0]
    return acronym == s
s=input("enter acronym")
words=input("enter words").split()
print(acronym_words(s, words))


def every_other(string):
    result=[]
    for i in range(1,len(string),2):
        result.append(string[i])
    return result
string=(input("enter a string"))
print(every_other(string))


def even_list(smaller_num, larger_num):
    result=[]
    for i in range(smaller_num, larger_num+1):
        if i%2==0:
            result.append(i)
    return result
smaller_num=(int(input("enter the small")))
larger_num=(int(input("enter the larger")))
print("the list of even number is:",even_list(smaller_num, larger_num))

def odd_list(smaller_num, larger_num):
    result=[]
    for i in range(smaller_num, larger_num+1):
        if i%2==1:
         result.append(i)
    return result
smaller_num=(int(input("enter the small")))
larger_num=(int(input("enter the larger")))
print("the list of odd number is:",odd_list(smaller_num, larger_num))


def factors_int(num):
    factors=[]
    for i in range(1, num+1):
        if num % i==0:
            factors.append(i)
    return factors
num=int(input("enter a number"))
print("the factors are:", factors_int(num))


def ascending_order(a,b,c):
    if a>b:
        a,b = b,a
    if b>c:
        b,c = c,b
    if a>b:
        a,b = b,a
    return a, b, c
a= int(input("enter a number"))
b= int(input("enter a number"))
c= int(input("enter a number"))
print(ascending_order(a,b,c))

def black_jack(cards):
    count=0
    for i in cards:
        if i in [2,3,4,5,6]:
            count+=1
        elif i in [7,8,9]:
            count+=0
        else:
            count+=-1
    return count
cards_input=input("enter the cards").split()
cards=[]
for c in cards_input:
    if c.isdigit:
        cards.append(int(c))
    else:
        cards.append(c.lower())
print(black_jack(cards))

def oddeven_war(numbers):
    odd=0
    even=0
    for i in numbers:
        if i % 2==0:
            odd+=i
        else:
            even+=i
    if odd>even:
        return ("odd wins")
    elif even>odd:
        return ("even wins")
numbers=list(map(int,input("enter the numbers").split()))
print("The winner is", oddeven_war(numbers))
'''

def addition_list(list1,list2):
    result=[]
    for i in range(len(list1)):
        result.append(list1)+(list2)
    return result
list1=list(map(int,input("enter the list").split()))
list2=list(map(int, input("enter the list").split()))
print("The addition is", addition_list(list1, list2))