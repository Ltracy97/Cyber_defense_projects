
chars ="abcdefghijklmnopqrstuvwxyz"
char_recorder = {}
num_recorder = {}
kill = False
for i in range(0,26):
    char_recorder[i] = chars[i]
    num_recorder[chars[i]] = i

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

                