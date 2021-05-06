# Веб-сервисы и микросервисная архитектура.
## Лабораторная работа №2
- Иннокентьев Владимир
- Фёдоров Байытаан

## Cодержание
- [Тема и задания](#theme)
- [Источники](#source)
- [Инструкция](#instruction)
- [Функции](#functions)

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
1) Открыть консоль в папке и прописать ```python -m venv venv```, будет создана папка _"venv"_
2) Активировать _**venv**_ через команду ```venv\scripts\activate```. В консоли должна появиться _"(venv)"_
3) Установить библиотеки из _"requirements.txt"_ командой ```pip install -r requirements.txt``` или каждую вручную ```pip install <название библиотеки>```
4) Скачать _**pgAdmin4**_ (это _**postgresql**_) и настроить свою базу<br>
	4.1. Пример БД лежит в файле _"shema.sql"_<br>
	4.2. Расписать данные под _**postgresql**_<br>
	4.3. Настроить внешний ключ по заданию. Пример:
```javascript
FOREIGN KEY (teamName) REFERENCES teams (teamName) ON DELETE CASCADE ON UPDATE CASCADE
```
  - первый _"teamName"_ относится к ```players```
  - второй _"teamName"_ относится к таблице ```teams```
  - ```ON DELETE CASCADE``` при удалении команды удаляет игроков 
  - ```ON UPDATE CASCADE``` при редактировании команды изменяет поле _"teamName"_ у игроков
  
5) Открыть _"main.py"_ и изменить 14-ю строку. 
  ```javascript
  engine = create_engine("postgresql://username:password@localhost/foldername")
  ```
  - ```username``` = имя пользователя _**pgAdmin**_
  - ```password``` = пароль от _**pgAdmin**_
  - ```localhost``` = менять, если у вас хост другой
  - ```foldername``` = название папки с проектом, в этом случае будет папка _"app"_

6) Скачать _**Postman**_ для проверки запросов.
7) Запустить программу с помощью ```py main.py``` (_"main.py"_ название исполняемого файла)
     Должен показать что-то вроде ```Running on http://127.0.0.1:5000/```

8) Если всё получилось, то заходите в _**Postman**_ и создаёте вкладку для запросов.
9) Пример (Если данных не будет, то он ничего не вернёт):<br>
Cтраница функции и значение, которое оно принимает
  ```python
  @app.route('/getplayer/<int:playerid>', methods=['GET'])
  ```
10) В _**Postman**_ выбираете метод **GET**, т.к. данная страница принимает метод **GET** и отправляете запрос 
```python
http://127.0.0.1:5000/getteamplayers/13
```

<a name="functions"><h2>Функции / Запросы для Postman</h2></a>
### POST
- Добавление игрока в таблицу
```python
http://127.0.0.1:5000/addplayer
```
```javascript
{
    "firstname": "firstname",
    "secondname": "secondname",
    "patronname": "patronname",
    "birthdate": "yyyy-mm-dd",
    "teamname": "teamname"
}
```
- Добавление команды в таблицу
```python
http://127.0.0.1:5000/addteam
```
```javascript
{
    "teamname": "teamname", 
    "homecity": "homecity", 
    "sponsors": "sponsors"
}
```
### GET
- Возвращение игрока по id
```python
http://127.0.0.1:5000/getplayer/<int:playerid>
```
- Возвращение всех игроков
```python
http://127.0.0.1:5000/getplayers
```
- Возвращение игрока по id с атрибутами его команды
```python
http://127.0.0.1:5000/getplayerteam/<int:idplayer>
```
- Возвращение команды по id
```python
http://127.0.0.1:5000/getteam/<int:teamid>
```
- Возвращение всех команд
```python
http://127.0.0.1:5000/getteams
```
- Возвращение команды по id с атрибутами всех игроков в команде
```python
http://127.0.0.1:5000/getteamplayers/<int:idteam>
```
### PUT
- Редактирование игрока по id
```python
http://127.0.0.1:5000/editplayer
```
```javascript
{
    "playerid": 1,
    "firstname": "firstname",
    "secondname": "secondname",
    "patronname": "patronname",
    "birthdate": "yyyy-mm-dd",
    "teamname": "teamname"
}
```
- Редактирование команды по id
```python
http://127.0.0.1:5000/editteam
```
```javascript
{
    "teamid": 1,
    "teamname": "teamname", 
    "homecity": "homecity", 
    "sponsors": "sponsors"
}
```
### DELETE
- Удаление игрока из таблицы по id
```python
http://127.0.0.1:5000/deleteplayer/<int:idplayer>
```
- Удаление команды из таблицы по id
```python
http://127.0.0.1:5000/deleteteam/<int:idteam>
```
