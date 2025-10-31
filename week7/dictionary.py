'''
#isogram
def is_isogran(word):
    word=word.lower()
    return len(word)==len(set(word))
word=input("enter a word")
print(is_isogran(word))
'''

#array numbers
def array_numbers(list):
    result=[]
    for i in list:
        i = result
        if result != i:
            return result
list=list(map(int,input("enter a list of numbers").split()))
print(array_numbers(list))
