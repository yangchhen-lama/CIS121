'''
#hailstone 1
def hailstone(first):
    hails=[first]
    while first>1:
        
        if first%2==0:
            first=first/2
        else:
            first=(first*3)+1
        hails.append(int(first))
    return hails
first=int(input("enter a number"))
print(hailstone(first))
'''

#19
def is_acronym(s, list_of_words):
    if len(s)!=len(list_of_words):
        return False
    first_letters=""
    for word in list_of_words:
            if word=="":
                return False
            
            first_letter = word[0]
    
            first_letter = first_letters + first_letter
    if first_letters != s:
         return False
    
    return True
            