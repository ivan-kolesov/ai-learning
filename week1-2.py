fruits = ["apple", "banana", "orange"]
user = {
    "name": "Ivan",
    "age": 30,
    "city": "Madrid",
}

print("Перебор списка через for:")
for fruit in fruits:
    print(fruit)

# Аналог в PHP:
# foreach ($fruits as $fruit) {
#     echo $fruit . PHP_EOL;
# }

print("\nПеребор словаря через for (ключи и значения):")
for key, value in user.items():
    print(f"{key}: {value}")

# Аналог в PHP:
# foreach ($user as $key => $value) {
#     echo $key . ": " . $value . PHP_EOL;
# }

fruits.append("mango")
user["country"] = "Spain"

print("\nПосле добавления элемента:")
print(fruits)
print(user)

# Аналог в PHP:
# $fruits[] = "mango";
# $user["country"] = "Spain";

fruits.remove("banana")
del user["age"]

print("\nПосле удаления элемента:")
print(fruits)
print(user)

# Аналог в PHP:
# unset($fruits[1]);
# $fruits = array_values($fruits); // если нужно переиндексировать массив
# unset($user["age"]);
