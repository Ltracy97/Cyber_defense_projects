'''
File Name: vigener.py
Author: Louis Tracy
last edit date: 6/9/2024
purpose: This program can take any message and Keyword and encrypt or decrypt 
(Keyword is required for decryption to work)
'''

"""
chars - a variable that contains a string of the English alphabet

char_recorder - an empty library that will contain key values in the form of integers
with its corresponding value are characters from the English Alphabet

num_recorder - an empty library that will use the English Alphabet as key values
and the stored values are integers

kill - a boolean variable that represents if the main program should be killed
"""


chars ="abcdefghijklmnopqrstuvwxyz"
char_recorder = {}
num_recorder = {}
kill = False

"""
the for look will fill both empty libraries.

char_recorder -  contain key values in the form of integers
with its corresponding value are characters from the English Alphabet

num_recorder - contain key values in the form of the English Alphabet
with its corresponding value are integers
"""

for i in range(0,26):
    char_recorder[i] = chars[i]
    num_recorder[chars[i]] = i


"""
endorde - takes an input from the user asking they want to encrypt, decrypt, or stop
the program

new_message - contains an empty string that will become the message after
encryption/decrption

keyword_array - an empty list that will contain integers that correspond to the postion
of each character in the keyword relative to the English Alphabet

shift - contains an integer that represents where the program is in the keyword_array
list

keyword - takes an input from the user. represents the keyword used in the
encryption/decryption

message - takes the message that is suppose to be encrpted/decrypted

summary: the program will prompt the user on wheter they wish to encrypt, decrypt, or
kill the program. If the user wants to encrypt/decrypt they will then be prompted for
the keyword and the message. The program then uses the num_recorder and ketword array
to convert the keyword into a list of integers to indicate the shift for each letter
in the message. After the program uses keyword_array, num_recorder, and char_recorder
to encrypt/decrypt that the single character of the message then append that character
into the new_character string then increments the shift variable by 1. After each conversion the program check if we have reached
the end of the keyword_array then we reset the shift variable to the front.




"""



while kill != True:
    enorde = input("enter if you want to encrypt or decrypt message or stop to kill the program: ")
    new_message = ""
    keyword_array = []
    shift = 0
    if enorde == "encrypt" or enorde == "Encrypt":
        keyword = input("enter your keyword?: ")
        message = input("enter message: ")
        for keys in keyword:
            if keys.isupper():
                keyword_array.append(num_recorder[keys.lower()])
            else:
                keyword_array.append(num_recorder[keys])
        for cycle in message:
            if cycle != " ":
                if cycle.isupper():
                    if shift >= len(keyword_array):
                        shift = 0
                    convert = num_recorder[cycle.lower()]
                    new_char = char_recorder[(convert + keyword_array[shift])%26]
                    new_message = new_message + new_char.upper()
                    shift = shift + 1
                else:
                    if shift >= len(keyword_array):
                        shift = 0
                    convert = num_recorder[cycle]
                    new_char = char_recorder[(convert + keyword_array[shift])%26]
                    new_message = new_message + new_char
                    shift = shift + 1
            else:
                new_message = new_message + " "
    
    elif enorde == "decrypt" or enorde == "Decrypt":
        keyword = input("enter your keyword?: ")
        message = input("enter message: ")
        for keys in keyword:
            if keys.isupper():
                keyword_array.append(num_recorder[keys.lower()])
            else:
                keyword_array.append(num_recorder[keys])
        
        for cycle in message:
            if cycle != " ":
                if cycle.isupper():
                    if shift >= len(keyword_array):
                        shift = 0
                    convert = num_recorder[cycle.lower()]
                    new_char = char_recorder[(convert - keyword_array[shift])%26]
                    new_message = new_message + new_char.upper()
                    shift= shift + 1
                else:
                    if shift >= len(keyword_array):
                        shift = 0
                    convert = num_recorder[cycle]
                    new_char = char_recorder[(convert - keyword_array[shift])%26]
                    new_message = new_message + new_char
                    shift = shift + 1
            
            else:
                new_message = new_message + " "
    
    elif enorde == "stop" or enorde == "Stop":
        kill = True
                
    else:
        print("wrong input")
    
    print(new_message)