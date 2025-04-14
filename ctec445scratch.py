import random
import string
import time

# Generate a secure password
def generate_password(length=12):
    if length < 12:
        print("Password must be at least 12 characters long.")
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for _ in range(length))
    return password

# Verify the strength of a password
def verify_password(password):
    if len(password) < 12:
        return "The password is weak, must contain at least 12 characters."

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if all([has_upper, has_lower, has_digit, has_special]):
        return "This password is strong, it meets all security requirements."
    else:
        return "This password is moderate. Include at least one uppercase, lowercase, number, and special character."

#One time password
def generate_otp():
    otp = random.randint(100000, 500000)
    print(f"Your OTP is: {otp}")

    start_time = time.time()

    while True:
        user_input = input("Enter the OTP: ")
        if not user_input.isdigit():
            print("Invalid input. Enter numbers only.")
            continue

        if time.time() - start_time > 60:
            print("OTP expired. Request a new one.")
            return False

        if int(user_input) == otp:
            print("OTP verified successfully!")
            return True
        else:
            print("Incorrect OTP, please try again.")

#User Interaction
while True:
    print("\nTesting options:")
    print("1: Try generating a secure password")
    print("2: Test password strength")
    print("3: Verify login with a One Time Password(OTP)")
    print("4: Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        password = generate_password()
        if password:
            print(f"Generated Password: {password}")

    elif choice == "2":
        user_password = input("Enter the password to check strength: ")
        print(verify_password(user_password))

    elif choice == "3":
        generate_otp()


    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please select a number between 1 and 4.")