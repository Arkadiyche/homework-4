# Ruiners автотесты

#### Команда:
Чекрыжов Аркадий <br>
Набиев Эрик

#### Переменные окружения:
BROWSER; <br>
LOGIN;  - Логин существующего пользователя <br>
PASSWORD; - Пароль существующего пользователя <br>
SIGNUP_LOGIN;  - Логин нового пользователя, который будет создаваться во время тестов <br>

#### Запуск:

```shell script
./grid.sh
./node.sh
 LOGIN=<...> PASSWORD=<...> SIGNUP_LOGIN=<....> python3 run_tests.py
```

#### Чеклист:
[jira](http://jira.bmstu.cloud/browse/QA-1066) Нас в команде двое, делали все вместе
