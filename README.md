# Веб-сервисы и микросервисная архитектура.
## Лабораторная работа №2
- Иннокентьев Владимир
- Фёдоров Байытаан

## Cодержание
- [Тема и задания](#theme)
- [Источники](#source)
- [Инструкция](#instruction)

<a name="theme"><h2>Тема: "Игроки и команды"</h2></a>
Приложение должно хранить данные о игроках и их командах.
Таблица с данными об игроках должна хранить:
- Фамилию, имя и отчество игрока
- Дату рождения
- Ссылку на команду в которой он числиться

Таблица с данными о команде должна хранить:
- Название команды
- Город базирования
- Перечень спонсоров через запятую

Для клиента REST API:
- При получении данных об игроке нужно вместо ссылки на команду следует добавить вложенный объект с атрибутами команды
- При получении данных о команде следует добавить список всех игроков с их атрибутами.

<a name="source"><h2>Источники</h2></a>
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/database/)
- [Flask: Using SQLite 3 with Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/)

<a name="instruction"><h2>Инструкция</h2></a>
1) Открыть консоль в папке и прописать ```python -m venv venv```, будет создана папка "venv"
2) Активировать venv через команду ```venv\scripts\activate```. В консоли должна появиться "(venv)"
3) Установить зависимости из "requirements.txt" командой ```pip install -r requirements.txt``` или каждую вручную ```pip install <название библиотеки>```
4) Скачать pgAdmin4 - это postgresql и настроить свою базу<br>
	4.1. Пример БД лежит в файле "shema.sql"<br>
	4.2. Расписать данные под postgresql<br>
	4.3. Настроить внешний ключ по заданию. Пример:
```javascript
FOREIGN KEY (teamName) REFERENCES teams (teamName) ON DELETE CASCADE ON UPDATE CASCADE
```
  - первый "teamName" относится к players
  - второй "teamName" относится к таблице "teams"
  - ```ON DELETE CASCADE``` при удалении команды удаляет игроков 
  - ```ON UPDATE CASCADE``` при редактировании команды изменяет поле "teamName" у игроков
  
5) Открыть "main.py" и изменить 14-ю строку. 
  ```javascript
  engine = create_engine("postgresql://username:password@localhost/foldername")
  ```
  - ```username``` = имя пользователя pgAdmina 
  - ```password``` = пароль от pgAdmina
  - ```localhost``` = менять, если у вас хост другой
  - ```foldername``` = название папки с проектом, в этом случае будет папка "app"

6) Скачать Postman для проверки запросов.
7) Запустить программу с помощью ```py main.py``` ("main.py" название исполняемого файла)
     Должен показать что-то вроде ```Running on http://127.0.0.1:5000/```

8) Если всё получилось, то заходите в Postman и создаёте вкладку для запросов.
9) Пример (Если данных не будет, то он ничего не вернёт):<br>
Cтраница функции и значение, которое оно принимает
  ```python
  @app.route('/getplayer/<int:playerid>', methods=['GET'])
  ```
   В постмане выбираете метод GET, т.к. данная страница принимает метод GET и отправляете запрос ```http://127.0.0.1:5000/getteamplayers/13```
