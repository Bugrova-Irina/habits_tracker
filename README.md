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

## Локальная установка:

1. Клонируйте репозиторий:
```
https://github.com/Bugrova-Irina/coursework_drf/
cd coursework_drf
```
Запустите все сервисы командой:
```
docker-compose up --build
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
Примените миграции:
```
python manage.py migrate
```
Запустите сервер:
```
python manage.py runserver
```

3. Для работы с отложенными задачами запустите Redis.

```celery -A config worker -l INFO -P eventlet``` - запуск worker.

```celery -A config beat -l info -S django``` - запуск beat.

## Использование:

После запуска сервера перейдите по ссылке http://127.0.0.1:8000/habits/.

## Продакшен развертывание
После каждого пуша в ветку develop автоматически запускается CI/CD пайплайн:
1. Тестирование - запуск линтеров и тестов.
2. Сборка - создание Docker образа.
3. Деплой - автоматическое обновление на сервере.

### Создайте сервер и настройте SSH доступ.

Добавьте секреты в GitHub (Settings -> Secrets and variables -> Actions):

DOCKER_HUB_USERNAME - ваш логин Docker Hub

DOCKER_HUB_ACCESS_TOKEN - токен Docker Hub

SSH_KEY - приватный SSH ключ для доступа к серверу

SSH_USER - пользователь сервера (например, irina-ubuntu)

SERVER_IP - IP адрес сервера

### Настройте сервер:

#### Создайте директорию проекта
```
sudo mkdir -p /opt/coursework_drf
```
```
sudo chown $USER:$USER /opt/coursework_drf
```

#### Скопируйте файлы проекта
```
cp docker-compose.yml nginx.conf deploy.sh /opt/coursework_drf/
```
```
cp .env /opt/coursework_drf/  # создайте .env с настройками
```
#### Дайте права на выполнение
```
chmod +x /opt/coursework_drf/deploy.sh
```

## Настройте автозапуск

```
sudo nano /etc/systemd/system/coursework_drf.service
```

## Проверка работоспособности
После деплоя проверьте:
### На сервере
```
cd /opt/coursework_drf
```

### Статус контейнеров
```
docker-compose ps
```
### Логи приложения
```
docker-compose logs backend
```
### Доступность приложения
```
curl http://localhost/admin/
```
### Управление контейнерами
#### Запуск
```
docker-compose up -d
```
#### Остановка
```
docker-compose down
```
#### Перезапуск
```
docker-compose restart
```
#### Просмотр логов
```
docker-compose logs -f
```

Продакшен версия доступна по адресу http://158.160.16.66/
**Если видите ошибку 404:**
- Это нормально - Django показывает 404 для корневого URL
- Проверьте другие эндпоинты:
  - http://158.160.16.66/admin/ - админка Django
  - http://158.160.16.66/users/login/ - авторизация
  - http://158.160.16.66/users/register/ - регистрация нового пользователя
  - http://158.160.16.66/habits/ - функционал привычек (доступен авторизованному 
  пользователю)
  - http://158.160.16.66/swagger/ - документация API
  - http://158.160.16.66/redoc/ - документация API

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