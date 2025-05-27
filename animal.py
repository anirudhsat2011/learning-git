import sys
import subprocess
import os

def play_sound(file):
    if os.path.exists(file):
        try:
            subprocess.run(["ffplay", "-nodisp", "-autoexit", file], check=True)
        except Exception as e:
            print(f"Error playing sound: {e}")
    else:
        print(f"Sound file '{file}' not found.")

def cat():
    print('Meow!')
    play_sound('cat.wav')

def dog():
    print('Woof!')
    play_sound('dog.wav')

def default():
    print('Hello')

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = input("Please enter an argument (e.g., 'cat' or 'dog'): ").strip()

    command = command.lower()

    if command == 'cat':
        cat()
    elif command == 'dog':
        dog()
    elif command == '':
        print('Please give an argument')
    else:
        default()

if __name__ == '__main__':
    main()

