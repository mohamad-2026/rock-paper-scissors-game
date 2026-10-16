def greet():
    print("سلام! به دنیای توابع خوش آمدی.")

greet()
greet()
greet()

def greet_person(name):
    print("سلام", name, "! به دنیای توابع خوش آمدی.")

greet_person("علی")
greet_person("مریم")
greet_person("رضا")

def add(a, b):
    return a + b

result = add(3, 5)
print("نتیجه:", result)

print("دو برابر نتیجه:", result * 2)
def double(n):
    return n * 2

def triple(n):
    return n * 3

x =double(5)
y =triple(x)
print(y)

def check_age(age):
    if age >= 18:
        return"بزرگسال"
    else:
        return"کودک"

    print(check_age(20))
    print(check_age(10))
    print(check_age(18))

    fruits = ["پرتقال"  "موز"  "سیب"]
    print(fruits)