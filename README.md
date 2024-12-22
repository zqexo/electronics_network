# Electronics Network API

Этот проект представляет собой платформу для управления торговой сетью по продаже электроники. Он включает API-интерфейс, админ-панель и использует иерархическую структуру для управления сетью.

---

## 📋 Описание проекта

**Особенности:**
- Иерархическая структура сети:
  - Завод (уровень 0).
  - Розничная сеть (уровень 1).
  - Индивидуальный предприниматель (уровень 2).
- Поддержка следующих данных для каждой сущности:
  - Название.
  - Контакты (email, страна, город, улица, номер дома).
  - Продукты (название, модель, дата выхода на рынок).
  - Поставщик (объект следующего уровня в иерархии).
  - Задолженность перед поставщиком.
  - Автоматическое указание времени создания.
- Админ-панель с фильтрацией по городу, ссылками на поставщиков и action для очистки задолженности.
- API:
  - CRUD для всех сущностей.
  - Ограничение обновления задолженности через API.
  - Фильтрация объектов по стране.
  - Ограничение доступа только для активных сотрудников.
- Документация API с использованием Swagger и ReDoc.
- Поддержка CORS для работы с внешними клиентами.

---

## 📂 Структура проекта
```users/``` — Приложение для управления пользователями.\
```network/``` — Приложение для работы с иерархией сети.\
```Network.postman_collection.json``` — Коллекция Postman запросов.

```
electronics_network/
├── electronics_network/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── network/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── .env
├── .env.docker
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Network.postman_collection.json
├── README.md
```

---

## 🛠️ Технологии

- **Backend:** Python 3.11, Django 4+, Django REST Framework.
- **База данных:** PostgreSQL.
- **Документация:** DRF-yasg.
- **Контейнеризация:** Docker, Docker Compose.

---

## 🚀 Установка и запуск

### 1. Склонируйте репозиторий
```bash
git clone https://github.com/zqexo/electronics_network.git
cd electronics_network
```
### 2. Настройте переменные окружения
Создайте файл .env.docker в корне проекта со следующим содержимым:
```
SECRET_KEY=
DEBUG=

CORS_ALLOW_ALL_ORIGINS=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```
### 3. Соберите и запустите контейнеры
- Сборка и запуск контейнеров:
```bash
docker-compose up --build
```
- Остановка контейнеров:
```bash
docker-compose down
```
- Создать суперпользователя:
```bash
docker-compose exec app python manage.py csu
```

### 4. Полезные ссылки

Админ-панель: ```http://localhost:8000/admin/``` \
Swagger-документация: ```http://localhost:8000/swagger/``` \
ReDoc-документация: ```http://localhost:8000/redoc/```

---

## 🧪 Тестирование

1. Установите Postman.
2. Импортируйте коллекцию Postman из репозитория.
3. Выполните тестовые запросы к API.

---

## 📞 Контакты

- #### Telegram: ```@zqexo```
  - #### Email: ```z@qexo.ru```