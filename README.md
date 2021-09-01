![yamdb_workflow](https://github.com/Viktrols/yamdb_final/actions/workflows/main.yml/badge.svg?branch=master)
# REST API для сервиса YaMDb — базы отзывов
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории (книги, фильмы и тд) Произведению может быть присвоен жанр из списка предустановленных (сказка, драма, артхаус и тд)

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Пользователи оставляют к произведениям текстовые отзывы и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения. К каждому отзыву можно оставить комментарий.
## Подготовка и запуск проекта
### Создать .env и заполнить переменные окружения:
```
SECRET_KEY=<секретный ключ проекта django>

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=<почтовый адрес или имя пользователя>
EMAIL_HOST_PASSWORD=<пароль>
DEFAULT_FROM_EMAIL=<почтовый адрес>

DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя базы данных postgres>
DB_USER=<имя пользователя>
DB_PASSWORD=<пароль>
DB_HOST=db
DB_PORT=5432

```
### Создать файл pg.env и заполнить переменные окружения для работы с Postgres:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя базы данных postgres>
DPOSTGRES_USER=<имя пользователя>
POSTGRES_PASSWORD=<пароль>
DB_HOST=db
DB_PORT=5432

```
### Собрать docker-compose:
```
docker-compose up -d --build
```
### Собрать статические файлы в STATIC_ROOT:
```
docker-compose exec web python3 manage.py collectstatic --noinput
```
### Применить миграции:
```
docker-compose exec web python3 manage.py migrate --noinput
```
### Заполнить базу данных:
```
docker-compose exec web python3 manage.py loaddata fixtures.json
```
### Создать суперпользователя Django:
```
docker-compose exec web python manage.py createsuperuser
```
### Проект будет доступен по адресу http://127.0.0.1
### Документация API http://127.0.0.1/redoc
### Образ на DockerHub https://hub.docker.com/repository/docker/viktrols/yamdb


