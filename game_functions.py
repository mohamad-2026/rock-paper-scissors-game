import random
import fa_console

def show_menu():
    print("=== بازی سنگ، کاغذ، قیچی ===")
    print("انتخاب کن: s برای سنگ، k برای کاغذ، g برای قیچی")
    print()

def get_user_choice():
    user_input = input("انتخاب تو: ")
    if user_input == "s":
        return "سنگ"
    elif user_input == "k":
        return "کاغذ"
    elif user_input == "g":
        return "قیچی"
    else:
        print("انتخاب نامعتبر!")
        return None

def get_computer_choice():
    choices = ["سنگ", "کاغذ", "قیچی"]
    return random.choice(choices)

def compare(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "مساوی شد!"
    elif user_choice == "سنگ" and computer_choice == "قیچی":
        return "تو بردی!"
    elif user_choice == "کاغذ" and computer_choice == "سنگ":
        return "تو بردی!"
    elif user_choice == "قیچی" and computer_choice == "کاغذ":
        return "تو بردی!"
    else:
        return "کامپیوتر برد!"

def play_game():
    show_menu()
    user_choice = get_user_choice()
    if user_choice is None:
        return
    computer_choice = get_computer_choice()
    print(f"کامپیوتر انتخاب کرد: {computer_choice}")
    result = compare(user_choice, computer_choice)
    print(result)

while True:
    play_game()
    play_again = input("\nدوباره بازی می‌کنی؟ (y/n): ")
    if play_again != "y":
        print("خداحافظ!")
        break