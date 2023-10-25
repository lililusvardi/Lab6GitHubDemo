# Lili Lusvardi
def main_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def encode(password):
    result = ""
    for index in password:
        num = int(index) + 3
        result += str(num)
    return result
def decode(encoded):
    result = ""
    for index in encoded:
        num = int(index) - 3
        result += str(num)
    return result
keepRunning = True

while keepRunning:
    main_menu()
    choice = int(input("Please enter an option:"))
    if choice == 1:
        password = input("Please enter your password to encode:")
        encoded = encode(password)
        print("Your password has been encoded and stored!\n")
    if choice == 2:
        decoded = decode(encoded)
        print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
    if choice == 3:
        break
