# Описание

Проект представляет собой API для размещения и просмотра постов и фотографий, которые объединены в различные тематические сообщества. Пост может сожержать текст и изображение. Пользователи могут оставлять комментарии к своим и чужим постам.

- Для просмотра постов, размещенных другими пользователями, регистрация не требуется. Для размещения постов
требуется регистрация и получение токена. Редактирование и удаление доступны только автору поста. Минимальное требование для размещения нового поста - текст(поле **"text"**), изображение необязательно(поле **"image"**).
- Для просмотра комментариев к постам, размещенных другими пользователями, регистрация не требуется. Для размещения комментариев
требуется регистрация и получение токена. Редактирование и удаление доступны только автору комментария. Минимальное требование для размещения нового комментария - текст(поле **"text"**).
- Список сообществ также доступен к просмотру неаутентифицированным пользователям, но составляется и модерируется администратором. Пользователь может определить сообщество к своему новому посту указав при отрпавке данных в поле **"group"** его номер, предварительно узнав в списке доступных сообществ.
- Пользователи могу быть подписаны друг на друга для быстрого поиска постов. Пользователь доступна информация только по его текущим подпискам.
Для использования данной функции требуется регистрация и наличие токена.
     
     

# Установка
## Как запустить проект:
### 1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Scorcer777/kittygram.git
cd kittygram
```
### 2. Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
### 3.Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
### 4. Запустить проект:
```
python3 manage.py runserver
```
# Примеры запросов

## 1. Получение токена.

Для получения токена необходимо отправить данные зарегистрированного пользователя
```
{
"username": "string",
"password": "string"
}
```
на URL адрес
```
http://127.0.0.1:8000/auth/jwt/create/
```
Ответ придет в виде токена:
```
"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MjM3NzgxOCwiaWF0IjoxNjkyMjkxNDE4LCJqdGkiOiIxM2RkOTg1ZTc1MTk0MGI5YmNmMDI2YmFkMmJhY2MxMSIsInVzZXJfaWQiOjF9._GbFYOfjJBxCanCbEB2Y4KLEuYNRR6kBdiObS8lKYO4",
"access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyNTUwNjE4LCJpYXQiOjE2OTIyOTE0MTgsImp0aSI6ImYzNjBhZDk4OWI4YjRjMGM4NDAzYjlhMmQ1NWM1MWYyIiwidXNlcl9pZCI6MX0.R3faMt6BV3KRTm49lessQw65uXck9a4Z4Dz8kWT0zrM"
```
где, access токен используется для аутентификации в API при отправке запросов посредством добавления его в параметр Authorization Bearer (далее сам токен), а refresh токен служит для обновления токена access по истечении его срока действия, который по умолчанию действует 3 суток.

## 2. Примеры запросов.

### Получение списков постов, комментариев, сообществ и подписок.
Отправить GET запрос URL
```
http://127.0.0.1:8000/posts/ (опционально можно указать параметры выдачи, offset - ID поста, которого начинается отображение, limit - количество постов на страницу. http://127.0.0.1:8000/posts/?offset=x&limit=y)
http://127.0.0.1:8000/posts/{id}/
http://127.0.0.1:8000/posts/{id}/comments/
http://127.0.0.1:8000/groups/
http://127.0.0.1:8000/groups/{id}/
http://127.0.0.1:8000/groups/
```
Пример успешного ответа:
Status 200 OK.
```
[
    {
        "id": 1,
        "text": "Richard",
        "pub_date": "2023-08-17T17:08:27.187812Z",
        "author": "Scorcer777",
        "image": "http://127.0.0.1:8000/posts/temp_faHPqGK.jpeg",
        "group": 1
    },
    {
        "id": 2,
        "text": "Pas dobar",
        "pub_date": "2023-08-17T17:13:33.030814Z",
        "author": "Scorcer777",
        "image": "http://127.0.0.1:8000/posts/pictures/temp.jpeg",
        "group": null
    },
]
```


### Создание поста, комментария.
**Создние поста**:
Отправить POST запрос URL
http://127.0.0.1:8000/posts/
```
{
     "text": "Richard.", **(обязательное поле)**
     "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAAEsCAIAAABi1XKVAAAAGXRFWH"
     "group": 1
}
```
Пример успешного ответа:
Status 201 Created.
```
{
     "id": 1,
     "text": "Richard",
     "pub_date": "2023-08-17T17:08:27.187812Z",
     "author": "Scorcer777",
     "image": "http://127.0.0.1:8000/posts/temp_faHPqGK.jpeg",
     "group": 1
}
```

**Создние комментария**:
Отправить POST запрос URL
http://127.0.0.1:8000/posts/{id}/
```
    {
        "text": "Комментарий аутентифицированного пользователя.", **(обязательное поле)**
    },
```
Пример успешного ответа:
Status 201 Created.
```
{
   "id": 1,
   "author": "Scorcer777",
   "text": "Комментарий аутентифицированного пользователя.",
   "created": "2023-08-17T17:43:12.112108Z",
   "post": 1
}
```
Документация с описанием всех эндпоинтов и запросов доспупна по адресу:
```
http://127.0.0.1:8000/redoc/
```
Отркывать при запущенном локально сервере.








