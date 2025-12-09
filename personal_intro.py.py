def get_nonempty_input(prompt):
    """Prompt until the user types something non-empty (after stripping)."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value — it can't be blank.")

        def get_valid_age(prompt):
    """Prompt until the user enters a valid positive integer age."""
    while True:
    s = input(prompt).strip()
    if not s:
    print("Please enter your age.")
    continue
    # allow numeric input only
    if s.isdigit():
    age = int(s)
    if age > 0:
    return age
    print("Age must be greater than 0.")
    else:
    print("Please enter a valid whole number for age (e.g. 25).")
  
        def main():
    print("👋 Hi! Let's get to know each other.")
    name = get_nonempty_input("What's your name? ")
    age = get_valid_age("How old are you? ")    
    hobby = get_nonempty_input("What's one hobby you enjoy? ")
    # Friendly welcome message
    print("\n---")
    print(f"Nice to meet you, {name}!")
    print(f"You're {age} years old — that's awesome.")
    print(f"It's great that you enjoy {hobby}. Keep having fun with it! 🎉"
    print("---\n")


if __name__ == "__main__":
    main()
