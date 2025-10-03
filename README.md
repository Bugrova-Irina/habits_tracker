# Трекер полезных привычек на DjangoRestFramework
В приложении созданы фикстуры тестовых пользователей и привычек (см ниже).

```python manage.py runserver``` - запуск веб-приложения. Ctrl+C - остановка сервера.

```python manage.py createadmin``` - создание суперпользователя.

```python manage.py export_users``` - выгрузка пользователей в json.

```python manage.py export_habits``` - выгрузка привычек в json.

```python manage.py loaddata users_export.json``` - загрузка данных о пользователях.

```python manage.py loaddata habits_export.json``` - загрузка данных о привычках.

## Описание:

Бэкенд веб-приложения трекера полезных привычек. У полезной привычки может быть либо
вознаграждение, либо связана приятная привычка. Время выполнения полезной привычки может 
быть не более 2х минут. Владелец привычки может ее просматривать, редактировать, удалять,
может просматривать список только своих привычек.
Авторизованные пользователи могут видеть список привычек, у которых есть признак публичной
привычки. У приятной привычки не может быть связанной привычки или вознаграждения. Нельзя 
выполнять привычку реже, чем 1 раз в 7 дней.

В приложении реализована работа с отложенными задачами. Раз в день пользователю отправляются
напоминания в телеграмм с напоминанием о том, какие привычки нужно выполнить сегодня.

Для приложения настроен CORS.

Для приложения настроен запуск всех сервисов через Docker Compose.
Настроен процесс CI/CD с использованием GitHub Actions.

## Требования к окружению:

Установите:
 - python 3.13.0
 - Poetry
 - Django
 - Pillow
 - python-dotenv
 - psycopg2 или psycopg2-binary
 - djangorestframework
 - djangorestframework-simplejwt
 - flake8
 - black
 - isort
 - coverage
 - drf-yasg
 - celery
 - django-celery-beat
 - eventlet (для Windows)
 - requests
 - redis
 - django-cors-headers

В качестве базы данных используется PostgreSQL

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/Bugrova-Irina/coursework_drf/
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
```
poetry shell
```
```
poetry add django
```
```
poetry add Pillow
```
```
poetry add psycopg2
```
```
poetry add python-dotenv
```
```
poetry add djangorestframework
```
```
poetry add djangorestframework-simplejwt
```
```
poetry add flake8
```
```
poetry add black
```
```
poetry add isort
```
```
poetry add coverage
```
```
poetry add drf-yasg
```
```
poetry add redis
```
```
poetry add celery
```
```
poetry add django-celery-beat
```
```
poetry add eventlet
```
```
poetry add requests
```
```
poetry add django-cors-headers
```

3. Для работы с отложенными задачами запустите Redis.

```celery -A config worker -l INFO -P eventlet``` - запуск worker.

```celery -A config beat -l info -S django``` - запуск beat.

## Использование:

После запуска сервера перейдите по ссылке http://127.0.0.1:8000/habits/.

## Тестирование:

Добавлено тестирование корректности работы CRUD привычек.
Запускается командой ```python manage.py test```
Посмотреть отчет о покрытии тестами:
```
coverage run --source='.' manage.py test
```
```
coverage report
```

## Документация:

Для проекта подключен и настроен вывод документации с помощью drf-yasg.
http://localhost:8000/swagger/
 для Swagger UI или 
http://localhost:8000/redoc/
 для Redoc.

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)