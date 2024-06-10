'''
File Name: caesar.py
Author: Louis Tracy
last edit date: 6/9/2024
purpose: This program can take any message and encrypt or decrypt 
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

shift - contains an integer that represents how many letters do we shift the beginning
of the English Alphabet

message - takes the message that is suppose to be encrpted/decrypted

summary: the program will prompt the user on wheter they wish to encrypt, decrypt, or
kill the program. If the user wants to encrypt/decrypt they will then be prompted for
the shift and the message. After the program uses num_recorder, and char_recorder
to encrypt/decrypt that the single character of the message then append that character
into the new_character string.




"""





while kill != True:
    enorde = input("enter if you want to encrypt or decrypt message or stop to kill the program: ")
    new_message = ""
    
    if enorde == "encrypt" or enorde == "Encrypt":
        shift = int(input("by how many letters do you want to shift the message?: "))
        message = input("enter message: ")
        for cycle in message:
            if cycle != " ":
                if cycle.isupper():
                    
                    convert = num_recorder[cycle.lower()]
                    new_char = char_recorder[(convert + shift)%26]
                    new_message = new_message + new_char.upper()
                else:
                    convert = num_recorder[cycle]
                    new_char = char_recorder[(convert + shift)%26]
                    new_message = new_message + new_char
            else:
                new_message = new_message + " "
    
    elif enorde == "decrypt" or enorde == "Decrypt":
        shift = int(input("by how many letters do you want to shift the message?: "))
        message = input("enter message: ")
        for cycle in message:
            if cycle != " ":
                if cycle.isupper():
                    
                    convert = num_recorder[cycle.lower()]
                    new_char = char_recorder[(convert - shift)%26]
                    new_message = new_message + new_char.upper()
                else:
                    convert = num_recorder[cycle]
                    new_char = char_recorder[(convert - shift)%26]
                    new_message = new_message + new_char
            
            else:
                new_message = new_message + " "
    
    elif enorde == "stop" or enorde == "Stop":
        kill = True
                
    else:
        print("wrong input")
    
    print(new_message)

                