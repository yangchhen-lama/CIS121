'''x= 'apple'
y= x
print(x)
print(y)

x+= 's'
print(x)
print(y)
'''
'''
x= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
y=x
print(x)
print(y)

x[4] = 'Funday'

print(x)
print(y)
'''
'''
days_of_the_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
#workdays= ["monday", "Tuesday", "wednesday", "thursday", "friday"]
workdays= list(days_of_the_week[0.5])
workdays.append('Saturday')
print(workdays)

lyst
#print(days_of_the_week[2])

'''

#WAP a fucntion that takes a string as an argument,
#returns a list containing all of the words in that string.

x= 'Peter Piper picked a peck of pickled peppers'
result = ['Peter', 'Piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']

def string_to_list(word):
    words = []
    found_word=""
    for letter in range (len(word)):
        if letter ==" ":
            words.append(found_word)
            found_word =" "
        else:
            found_word += letter
    words.append(found_word)
    return words

def string_to_list_alt(word):
    words=
    found_word = ""
    for index in range(len(word)):
        if word[index] =="":
            words.append(found_word)
            found_word = "" 
        elif index == len(word)-1:


    #find the workds

    #add them to list

    ##
    def string_to_list_with_vowels(word):
        words = []
        #collect a word
        build_word= ''
        vowel_count = 0
        for letter in word:
            if letter == '':
                if vowel_count >= 2:
                #add built_word into the list
                words.append(build_word)
            build_word= ''
            vowel_count=0
        else:
            built_word += letter
            if letter in 'aeiou':
                vowel_count += 1
        words.append(build_word)
        return words
    
my_word = 'Peter Piper picked a peck of pickled peppers'
print (string_to_list_with_vowels(my_word))