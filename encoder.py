# Javier Hidalgo-Gato
def encode(password):
    encoded_pass = ""
    for char in password:
        encoded_pass = encoded_pass + str((int(char) + 3) % 10)
    return encoded_pass

def decode(password):


def main():
    while True:
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")
        choice = input("Please enter an option: ")
        if choice == 1:
            password = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        elif choice == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")
        elif choice == 3:
            break
        else:
            print("Invalid choice")
        print()

main()
