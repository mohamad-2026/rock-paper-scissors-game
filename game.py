import random

print("=== بازی سنگ، کاغذ، قیچی ===")
print("انتخاب کن: سنگ، کاغذ یا قیچی")
print()

user_choice = input("انتخاب تو: ")

choices = ["سنگ", "کاغذ", "قیچی"]
computer_choice = random.choice(choices)
print(f"کامپیوتر انتخاب کرد: {computer_choice}")
print()

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