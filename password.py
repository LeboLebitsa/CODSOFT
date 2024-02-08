import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    print("Welcome to the Password Generator.")
    length = int(input("How many characters would you like your password to have: "))

    if length <= 0:
        print("Invalid input, password length must be greater than zero")
    else:
        password = generate_password(length)
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()