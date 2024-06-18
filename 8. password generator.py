import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
