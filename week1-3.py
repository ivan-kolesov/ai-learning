def calculate_total(price, quantity, discount):
    return price * quantity - discount


print("Функция с несколькими аргументами и return:")
total = calculate_total(100, 3, 50)
print(total)

# Аналог в PHP:
# function calculateTotal($price, $quantity, $discount) {
#     return $price * $quantity - $discount;
# }
# echo calculateTotal(100, 3, 50) . PHP_EOL;


def greet_user(name, greeting="Привет"):
    return f"{greeting}, {name}!"


print("\nФункция с дефолтным значением аргумента:")
print(greet_user("Ivan"))
print(greet_user("Ivan", "Здравствуйте"))

# Аналог в PHP:
# function greetUser($name, $greeting = "Привет") {
#     return $greeting . ", " . $name . "!";
# }
# echo greetUser("Ivan") . PHP_EOL;
# echo greetUser("Ivan", "Здравствуйте") . PHP_EOL;


score = 82

print("\nУсловие if / elif / else:")
if score >= 90:
    print("Отлично")
elif score >= 75:
    print("Хорошо")
else:
    print("Нужно потренироваться")

# Аналог в PHP:
# if ($score >= 90) {
#     echo "Отлично";
# } elseif ($score >= 75) {
#     echo "Хорошо";
# } else {
#     echo "Нужно потренироваться";
# }


user = {
    "name": "Ivan",
    "city": "Madrid",
}
fruits = ["apple", "banana", "orange"]

print("\nПроверка наличия ключа в словаре и элемента в списке:")
if "city" in user:
    print('Ключ "city" есть в словаре')
else:
    print('Ключа "city" нет в словаре')

if "banana" in fruits:
    print('Элемент "banana" есть в списке')
else:
    print('Элемента "banana" нет в списке')

# Аналог в PHP:
# if (array_key_exists("city", $user)) {
#     echo 'Ключ "city" есть в массиве' . PHP_EOL;
# }
# if (in_array("banana", $fruits)) {
#     echo 'Элемент "banana" есть в массиве' . PHP_EOL;
# }
