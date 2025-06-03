import sys

def cat():
    print('Meow!')

def dog():
    print('Woof!')

def default(user_input):
    print('Hello, ' + user_input)

def main():
    if len(sys.argv) < 2:
        user_input = input('Enter an argument (cat/dog): ').strip()
        while not user_input:
            user_input = input('Enter an argument (cat/dog): ').strip()
    else:
        user_input = sys.argv[1].strip()

    input_lower = user_input.lower()

    if input_lower == 'cat':
        cat()
    elif input_lower == 'dog':
        dog()
    else:
        default(user_input)

if __name__ == '__main__':
    main()
