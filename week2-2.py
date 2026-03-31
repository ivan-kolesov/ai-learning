try:
    import requests
except ImportError:
    print("Библиотека requests не найдена.")
    print("Если вы используете uv, запустите так:")
    print("uv run --with requests python week2-2.py")
    print("Или создайте окружение и установите пакет:")
    print("uv venv")
    print("source .venv/bin/activate")
    print("uv pip install requests")
    raise SystemExit(1)


print("Установка библиотеки requests через uv:")
print("uv pip install requests")
print("Или разовый запуск без установки:")
print("uv run --with requests python week2-2.py")

url = "https://api.github.com/users/ivan-kolesov"

print("\nHTTP GET-запрос к публичному API и получение JSON:")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    user_data = response.json()

    print("JSON успешно получен")
    print(f"Логин: {user_data['login']}")
    print(f"Имя: {user_data.get('name')}")
    print(f"Профиль: {user_data['html_url']}")
    print(f"Публичных репозиториев: {user_data['public_repos']}")
except requests.exceptions.HTTPError as error:
    print(f"HTTP ошибка: {error}")
except requests.exceptions.ConnectionError as error:
    print(f"Ошибка соединения: {error}")
except requests.exceptions.Timeout as error:
    print(f"Таймаут запроса: {error}")
except requests.exceptions.RequestException as error:
    print(f"Ошибка запроса: {error}")
except ValueError as error:
    print(f"Ошибка разбора JSON: {error}")


# Аналог в PHP с cURL:
# $url = "https://api.github.com/users/ivan-kolesov";
# $ch = curl_init($url);
# curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
# curl_setopt($ch, CURLOPT_HTTPHEADER, ["User-Agent: PHP"]);
#
# try {
#     $result = curl_exec($ch);
#
#     if ($result === false) {
#         throw new Exception(curl_error($ch));
#     }
#
#     $data = json_decode($result, true, 512, JSON_THROW_ON_ERROR);
#     echo "Логин: " . $data["login"] . PHP_EOL;
#     echo "Профиль: " . $data["html_url"] . PHP_EOL;
#     echo "Публичных репозиториев: " . $data["public_repos"] . PHP_EOL;
# } catch (Exception $error) {
#     echo "Ошибка: " . $error->getMessage() . PHP_EOL;
# } finally {
#     curl_close($ch);
# }
