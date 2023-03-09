def Encoder(password):
    encoded_pass = ""
    for char in password:
        encoded_pass = encoded_pass + str((int(char) + 3) % 10)
    return encoded_pass
