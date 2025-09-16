# Трекер полезных привычек на DjangoRestFramework
```python manage.py runserver``` - запуск веб-приложения. Ctrl+C - остановка сервера.

```python manage.py createadmin``` - создание суперпользователя

```python manage.py export_users``` - выгрузка пользователей в json

```python manage.py export_habits``` - выгрузка привычек в json

```python manage.py loaddata users_export.json``` - загрузка данных о пользователях.

```python manage.py loaddata habits_export.json``` - загрузка данных о привычках.

```python manage.py test``` - запуск тестов

http://127.0.0.1:8000/materials/subscription/ - в Postman задайте метод POST и отправьте
запрос, например:
```
{
    "user": 2,
    "subscribe_course": "1",
    "status": "True"
}
```
Подписка на курс будет либо удалена, либо добавлена.

http://127.0.0.1:8000/users/payments?ordering=-payment_date - в Postman сортировка оплат
по дате платежа в порядке убывания

http://127.0.0.1:8000/users/payments?ordering=payment_date - в Postman сортировка оплат
по дате платежа в порядке возрастания

http://127.0.0.1:8000/users/payments?paid_course=2 - в Postman фильтруем по оплаченному
курсу с id=2

http://127.0.0.1:8000/users/payments?paid_lesson=3 - в Postman фильтруем по оплаченному
уроку с id=3

http://127.0.0.1:8000/users/payments?payment_type=transfer - в Postman фильтруем по типу
оплаты transfer

celery -A config worker -l INFO -P eventlet - запуск worker

celery -A config beat -l info -S django - запуск beat

## Описание:

Бэкенд веб-приложения трекера полезных привычек.


## Требования к окружению:

Установите:
 - python 3.13.0
 - Poetry
 - Django
 - Pillow
 - python-dotenv
 - psycopg2 или psycopg2-binary
 - djangorestframework
 - django-filter
 - djangorestframework-simplejwt
 - flake8
 - black
 - isort
 - coverage
 - drf-yasg
 - stripe
 - forex-python
 - celery
 - django-celery-beat
 - eventlet (для Windows)
 - requests

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
poetry add django-filter
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
poetry add stripe
```
```
poetry add forex-python
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
3. Запустите Redis

## Использование:

После запуска сервера перейдите по ссылке http://127.0.0.1:8000/materials/.

## Тестирование:

Добавлено тестирование корректности работы CRUD уроков и функционала работы подписки
на обновления курса. Добавлен отчет о покрытии тестами в папке htmlcov/index.html.

## Документация:

Для проекта подключен и настроен вывод документации с помощью drf-yasg.

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)