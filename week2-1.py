import json


class UserProfile:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        return f"Меня зовут {self.name}, я живу в городе {self.city}."

    def change_city(self, new_city):
        self.city = new_city


print("Простой класс с __init__, атрибутами и методами:")
user = UserProfile("Ivan", "Madrid")
print(user.introduce())
user.change_city("Barcelona")
print(user.introduce())

# Аналог в PHP:
# class UserProfile {
#     public $name;
#     public $city;
#
#     public function __construct($name, $city) {
#         $this->name = $name;
#         $this->city = $city;
#     }
#
#     public function introduce() {
#         return "Меня зовут {$this->name}, я живу в городе {$this->city}.";
#     }
#
#     public function changeCity($newCity) {
#         $this->city = $newCity;
#     }
# }
#
# $user = new UserProfile("Ivan", "Madrid");
# echo $user->introduce() . PHP_EOL;
# $user->changeCity("Barcelona");
# echo $user->introduce() . PHP_EOL;


text_file = "week2_text.txt"

with open(text_file, "w", encoding="utf-8") as file:
    file.write("Привет, это текстовый файл.\n")
    file.write("Здесь хранится вторая строка.")

print("\nЗапись и чтение текстового файла:")
with open(text_file, "r", encoding="utf-8") as file:
    text_content = file.read()

print(text_content)

# Аналог в PHP:
# $textFile = "week2_text.txt";
# file_put_contents($textFile, "Привет, это текстовый файл.\nЗдесь хранится вторая строка.");
# $textContent = file_get_contents($textFile);
# echo $textContent . PHP_EOL;


json_file = "week2_data.json"
data = {
    "name": "Ivan",
    "city": "Madrid",
    "skills": ["Python", "PHP"],
}

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("\nЗапись и чтение JSON-файла:")
with open(json_file, "r", encoding="utf-8") as file:
    json_content = json.load(file)

print(json_content)

# Аналог в PHP:
# $jsonFile = "week2_data.json";
# $data = [
#     "name" => "Ivan",
#     "city" => "Madrid",
#     "skills" => ["Python", "PHP"],
# ];
#
# file_put_contents(
#     $jsonFile,
#     json_encode($data, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT)
# );
#
# $jsonContent = json_decode(file_get_contents($jsonFile), true);
# print_r($jsonContent);
