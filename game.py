import random
import fa_console

print("=== بازی سنگ، کاغذ، قیچی ===")

while True:
    print()
    print("انتخاب کن: s برای سنگ، k برای کاغذ، g برای قیچی")
    user_input = input("انتخاب تو: ")

    if user_input == "s":
        user_choice = "سنگ"
    elif user_input == "k":
        user_choice = "کاغذ"
    elif user_input == "g":
        user_choice = "قیچی"
    else:
        print("انتخاب نامعتبر! فقط s یا k یا g رو بزن.")
        continue

    choices = ["سنگ", "کاغذ", "قیچی"]
    computer_choice = random.choice(choices)
    print(f"کامپیوتر انتخاب کرد: {computer_choice}")

    if user_choice == computer_choice:
        print("مساوی شد!")
    elif user_choice == "سنگ" and computer_choice == "قیچی":
        print("تو بردی!")
    elif user_choice == "کاغذ" and computer_choice == "سنگ":
        print("تو بردی!")
    elif user_choice == "قیچی" and computer_choice == "کاغذ":
        print("تو بردی!")
    else:
        print("کامپیوتر برد!")

    play_again = input("\nدوباره بازی می‌کنی؟ (y/n): ")
    if play_again != "y":
        print("خداحافظ!")
        break