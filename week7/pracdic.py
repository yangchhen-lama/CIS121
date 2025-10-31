'''
def iso(word):
    word= word.lower( )
    return len(set(word))== len(word)
word=input("enter a word:")
print (iso(word))


def uniquenum(number):
    unique=[]
    for num in number:
        if number.count(num) == 1:
            unique.append(num)
    return unique
number= list(map(int, input ("Enter numbers").split()))
print ("unique numbers:", uniquenum(number))


def unique(number):
    unique=[]
    for num in number:
        if number.count(num)== 1:
            unique.append(num)
    return unique
number=list(map(int, input ("enter number separated by spaces"). split()))
print ("unique 2 numbers", unique(number))

def dicti(name):
    return list(name.values())
name=input("enter list of dict")
hehe=eval(name)
print(dicti(hehe))
'''
def word_count(word):
    count={}
    for i in word:
        count[i]= count.get(i, 0)+1
    return count
word= input("enter a word")
print (word_count(word))
 