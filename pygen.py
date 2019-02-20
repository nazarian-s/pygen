import random

def generate(length, alphabet = [chr(i) for i in range(32, 127)]):
    return ''.join([random.choice(alphabet) for i in range(length)])

print("=== Strong Password Generator ===")

while True:

    gotLength = False
    while not gotLength:
        try:
            length = int(input("\nLength of each password: "))
            if length > 0:
                gotLength = True
            else:
                print("Please enter a positive number...")
        except ValueError:
            print("Please enter a valid number...")



    gotNumber = False
    while not gotNumber:
        try:
            number = int(input("\nHow many passwords would you like to generate ? "))
            if number> 0:
               gotNumber = True 
            else:
                print("Please enter a positive number...")
        except ValueError:
            print("Please enter a valid number...")
    print('\n')

    for i in range(number):
        print(generate(length))

    print('\n')

    gotAgain = False
    while not gotAgain:
        again = input("Continue ? [y/N] ")
        if again.lower().strip() in ['n', 'no', 'stop', 'exit', 'end']:
            exit(0)
        elif again.lower().strip() in ['y', 'yes', 'continue']:
            gotAgain = True

