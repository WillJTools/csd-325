# William Judd
6/14/2026
# Module 2.2 Assignment
# Password Strength Checker


def calculate_score(password):
    """Calculate a strength score based on basic password rules."""
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1

    return score


def classify_password(score):
    """Return a password rating based on the score."""
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    """Run the password strength checker program."""
    print("Password Strength Checker")
    password = input("Enter a password to check: ")

    score = calculate_score(password)
    rating = classify_password(score)

    print("Password score:", score)
    print("Password rating:", rating)


if __name__ == "__main__":
    main()
