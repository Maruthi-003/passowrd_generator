import random

def generate_password(length):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_char = "!@#$%^&*()_+{}[]?"
    all_chars = lower + upper + numbers + special_char

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(numbers),
        random.choice(special_char)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.sample(all_chars, length - 4)

    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)

    return "".join(password)

def main():
    print("RANDOM PASSWORD GENERATOR")
    try:
        n = int(input("Number of times you want to generate password: "))
        length = int(input("Enter the desired password length (minimum 4): "))

        if length < 4:
            print("Password length should be at least 4.")
            return

        for _ in range(n):
            print(generate_password(length))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
