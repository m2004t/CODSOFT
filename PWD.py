import string
import random
def get_user_input():
    length = int(input("Enter the length of the password: "))
    return length
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
def display_password(password):
    print("Generated Password:", password)
def main():
    length = get_user_input()
    password = generate_password(length)
    display_password(password)
if __name__ == "__main__":
    main()
