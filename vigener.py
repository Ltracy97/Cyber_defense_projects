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