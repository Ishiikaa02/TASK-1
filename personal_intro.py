# personal_intro.py - Personal Introduction Program

def main():
    """Main function to run the personal introduction program."""
    # Display welcome banner
    print("=" * 50)
    print("🌟 PERSONAL INTRODUCTION PROGRAM 🌟")
    print("=" * 50)
    
    # Get user information using input()
    name = input("What's your name? ")
    age = input(f"Hello {name}! How old are you? ")
    hobby = input("What's your favorite hobby? ")
    
    # Additional question (beyond the required 3)
    favorite_color = input("What's your favorite color? ")
    
    # Display friendly welcome message
    print("\n" + "=" * 50)
    print("✨ YOUR PERSONALIZED WELCOME MESSAGE ✨")
    print("=" * 50)
    print(f"\nWelcome, {name}! 👋")
    print(f"It's great to meet someone who's {age} years young!")
    print(f"I love that you enjoy {hobby} - that sounds amazing!")
    print(f"{favorite_color} is a wonderful color choice!")
    print("\nThank you for sharing about yourself!")
    print("=" * 50)

# Run the program if this file is executed directly
if __name__ == "__main__":
    main()
