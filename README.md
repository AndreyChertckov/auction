# Auction
Классический английский аукцион, разработан на Python + Django + Postgres + Celery

## Архитектура
Система состоит из трех приложений:
1. Core - Здесь хранятся основныек модели, такие как Auction и Bet, также в core представленны Serializer и Views
2. Users - Здесь представленна обновленая модель User и UserManager, это нужно чтобы убрать username и оставить только email, чтобы у каждого пользователя бы email
3. Mail sender - это приложение ответсвенно за отправку email сообщений поьзователям. Основная логика реализована в `tasks.py`, и выполняется как celery задачи

## Как запустить

### Env перменные

Для запуска сервера и celery необходимы следющие переменные окружения, данные переменые нужно занести в `.env`
|  Переменная окружения | Описание |
| -------- | -------- |
| `ADDRESS` | Адресс где запущена API |
| `DEBUG` | 1 если запустить в режиме дебаг ингаче пустая строка |
| `SECRET_KEY` | Секретный ключ django |
| `DB_HOST` | Имя хоста базы данных  |
| `DB_NAME` | Название базы postgres |
| `DB_USER` | Пользователь базы данных |
| `DB_PASSWORD` | Пароль базы данных |
| `BROKER_URL` | Адресс rabbitmq для celery |
| `EMAIL_HOST` | Аддресс smpt сервера |
| `EMAIL_PORT` | Порт на котором запущен smpt сервер |
| `EMAIL_HOST_USER` | Пользователь, от которого будут отправляться сообщения |
| `EMAIL_HOST_PASSWORD` | Пароль для доступа к отправке писем |

После того как переменные окружения будут в `.env`, необходимо вызвать следующую комманду, чтобы переменные окружения подтянулись в текущую сессию
```bash
export $(xargs < .env)
```
### Установка зависимостей
1. Создать окружение с версией python 3.9
2. `pip install -r requirements.txt`

### Миграции базы данных
Для того чтобы смигрировать базу данных необходимо вызвать
```bash
python manage.py migrate
```

### Запуск на хостовой машине
Для запуска django сервера можно воспользовать django-admin коммандой
```bash
python manage.py runserver
```
Для запуска celery можно воспользоваться 
```bash
celery -A auction worker -l INFO
```

### Запуск с использованием docker-compose
Для запуска с использванием `docker-compose` переменые должны быть представлены в `.env`. 
Необходимо заменить `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` на `postgres`, `BROKER_URL` должен быть заменен на `amqp://guest:guest@rabbit:5672//`

После заменны запустить 
```bash
docker-compose up --build -d 
```
Сервис бужет доступен на `8080` порту

Для созданияя суперпользователя можно воспользоваться следующей коммандой:
```bash
docker-compose exec app python manage.py createsuperuser
```

## Описание API
[Swagger](https://app.swaggerhub.com/apis/wselfjes/AuctionAPI/1.0.0)
