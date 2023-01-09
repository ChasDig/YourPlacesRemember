# Проект для создания своих воспоминаний:
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=My+Place+Memories)](https://git.io/typing-svg)
## Описание проекта:
### Небольшой проект написанный с использованием Django API:
Позволяет авторизоваться пользователю через свой аккаунт
Вконтакте или Google.
#### Главная страница сайта перед авторизацией:
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/1.png)

После завершения авторизации, пользователь попадает на главную страницу сайта с предоставлением всех ранее
опубликованных воспоминаний в порядке их публикации (если ранее пользователь не публиковал воспоминание, будет выведено предложение
опубликовать свое первое воспоминание.)
#### Главная страница после авторизации с ранее опубликованными воспоминаниями пользователя:
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/2.png)

#### Главная страница после авторизации, если у пользователя нет ранее опубликованных воспоминаний:
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/3.png)

В верхней части главной страницы(navbar) отображено название сайта, аватар пользователя и его nickname, импортированный из его аккаунта
(Вконтакте или Google), а также поле, для поиска воспоминания по названию:
#### Navbar:
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/4.png)

При нажатии на свой nickname, пользователь может выйти из своей учетной записи (при выходе, пользователь попадает
в главное меню с предложением авторизоваться, показанное ранее), а также создать новое воспоминание:
#### Dropdown menu:
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/5.png)

При создании воспоминания, пользователю предлагается заполнить информацию о своем воспоминании и добавить адрес места
воспоминания (после выбора места на карте, его адрес отображается в требуемом поле):
#### Создание воспоминания:
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/6.png)

После его создания, пользователь попадает на главное меню, где уже отображается новое воспоминание. При желании,
пользователь может удалить воспоминание или открыть его страничку, выбрав соответствующие кнопки, а также можно использовать поиск, чтобы найти старые воспоминания:
#### Новое воспоминание/поиск ранее опубликованного (даже при использовании поиска, под navbar-ом выводится три последних опубликованных воспоминания):
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/7.png)

#### Страница с подробным описанием воспоминания:
![Image alt](https://github.com/ChasDig/YourPlacesRemember/blob/master/readme_images/8.png)

## Подготовка проекта:

### Ссылка на проект в DockerHub:
https://hub.docker.com/r/chasdig/places_memories

### Запуск проекта используя docker-compose:
- Создаем образ (<b>images</b>) docker с именем <b>place_memories_web</b> и запускаем контейнер
в режиме daemon:
```shell
docker-compose up --build -d
```
- Закрываем соединение с docker-compose:
```shell
docker-compose down
```
- Удаляем образ (<b>images</b>):
```shell
docker rmi chasdig/places_memories 
```

### Запуск проекта используя Dockerfile:
- Создаем образ (<b>images</b>) docker с именем <b>place_memories_app</b>:
```shell
docker build -t place_memories_app .
```
- Запускаем container на основе образа с именем <b>place_memories_app</b> в режиме daemon:
```shell
docker run --name place_memories_app -p 8000:8000 -d place_memories_app
```

#### После ознакомления с проектом, мы можем остановить container docker и удалить container и images:
```shell
docker stop place_memories_app
```
```shell
docker rm place_memories_app
```
```shell
docker rmi place_memories_app
```

### Прямая настройка и запуск проекта:
- Установка зависимостей:
```shell
pip install -r requirements.txt
```
Т.к. используется SQLite, то дополнительных манипуляций с БД не требуется.
- Генерируем миграции:
```shell
python3 manage.py makemigrations
```
- Исполняем миграции:
```shell
python3 manage.py migrate
```
- Запускаем проект на локальном сервере:
```shell
python3 manage.py runserver
```
- При необходимости, создаем суперпользователя для работы в качестве администратора:
```shell
python3 manage.py createsuperuser
```

## Тестирование проекта:
- Для выполнения тестирования всего проекта:
```shell
./manage.py pytest .
```
- - Также можно провести тестирование всего проекта, используя пакет <b>coverage<b>:
```shell
coverage run --source='.' ./manage.py test . 
```
- - После чего посмотреть процент покрытия нашего приложения тестами:
```shell
coverage report
```
