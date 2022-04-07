# cities_app

docker-compose up -d --build

Для удобвства тестирования в образ добавлена sqlite с данными

Авторизационные данные admin Test1111

Ссылка на приложение http://localhost:8000/

## api 
### Получение всего списка
http://localhost:8000/api/cities/?name=Bel 

Где ?name=Bel часть имени по которому будет осуществляться поиск
### Получение города по id

http://localhost:8000/api/city/1/
