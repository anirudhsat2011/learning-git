import sys

def cat():
    print('Meow!')

def dog():
    print('Woof!')

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

