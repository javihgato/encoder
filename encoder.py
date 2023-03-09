def encoder(password):
    encoded_pass = ""
    for char in password:
        encoded_pass = encoded_pass + str((int(char) + 3) % 10)
    return encoded_pass


def decoder(password):
    decoded_pass = ""
    for char in password:
        decoded_pass = decoded_pass + str((int(char) + 7) % 10)
    return decoded_pass


def main():
    while True:
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Enter an 8-digit password: ")
            print("Encoded password is", encoder(password))
        elif choice == "2":
            password = input("Enter an already encoded 8-digit password: ")
            print("Decoded password is", decoder(password))
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()

main()
