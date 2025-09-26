
#Created by Yangchhen Lama
#1. Zyra the code mage has hidden a mysterious cipher in reversed messages. You must help Zyra uncover
#the secrets of the digital realm. Create a function called reverse string that takes the variable word
#(a string) and returns the word in reversed order


def reverse_string(word):
    return word[::-1]

word=input("enter a word")
print ("The reverse is :", reverse_string(word))

# The normal human body temperature is 98.6F in Fahrenheit and 37C in Celsuis. Create a function
t#hat determines if the temp is considered a fever(anove normal body temperature) or not. temp will
#be measured in Fahrenheit and Celsuis.

def is_fever(input_temp):
    output = False
#1 how can we extract the unit? F or C
    unit = input_temp[:-1]

#2 How can we extract the temperature?
    temperature= int(input_temp[:-1])

#3. If it is F, > 98.6 = fever
    if unit == "F" and temperature > 98.6:
      output = True

#4. If it is C, > 37.0 = fever
    elif unit == "c" and temperature > 37:
     output = True

    return output
userinput = input("enter a temp 00F , 00C:")
print(f"This temp {userinput} is fever? {is_fever(userinput)}")


#The boiling point of water is 212F in Fahrenheit and 100C in Celsuis. Create a function that
#determines if the temp is considered boiling or not. temp will be measured in Fahrenheit and Celsuis.
#Notice: The F or C will always be the last character in the string

def hamming_distance(str1, str2):
    
    count = 0

    if len(str1) != len(str2):
       #dont run if words are not same length
       return 0
    #literate through each stringm since both strings are same
    for letterPos in range(len(str1)):
       #if a letter is different, then we +1
       if str1[letterPos] != str2[letterPos]:
          count += 1
    #Done
    return count

input1= input("string 1:")
input2= input("string 2:")
print(f"Distance = {hamming_distance(input1, input2)}")

#question 8

def last_letters(sentence):
   encode=""
   #1. How to iterature through the characters
   for pos in range(0, len(sentence)):
   #how can we know the last letter of each word?
   #"wingardium levios makes objects float"
        if sentence[pos + 1] == " ":
           encode +=sentence[pos]
   #3. How do we store the last characters and output it.
   return encode + sentence[-1]
user_input = input("enter a spell")
print(f"Encoded spell is {last_letters(user_input)}")

   