# Javier Hidalgo-Gato
def encode(password):
    encoded_pass = ""
    for char in password:
        encoded_pass = encoded_pass + str((int(char) + 3) % 10)
    return encoded_pass


def decode(password):
    decoded_pass = ""
    for char in password:
        decoded_pass = decoded_pass + str((int(char) + 7) % 10)
    return decoded_pass


def main():
    password = 0
    while True:
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = str(input("Please enter an option: "))
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