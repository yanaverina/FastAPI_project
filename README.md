# 🔗 URL Shortener API

Простое и удобное API для сокращения длинных URL-адресов с аутентификацией пользователей и статистикой переходов.


## 🚀 Возможности

- Создание коротких ссылок
- Пользовательские алиасы для ссылок
- Ограничение срока действия ссылок
- Статистика переходов
- Аутентификация пользователей
- Автоматическая очистка неиспользуемых ссылок по истечении 5 дней

## 📚 Документация API

### 🔐 Аутентификация

| Метод | Эндпоинт     | Описание                          | Требуется аутентификация |
|-------|--------------|-----------------------------------|--------------------------|
| POST  | `/register`  | Регистрация нового пользователя   | Нет                      |
| POST  | `/login`     | Вход в систему                    | Нет                      |
| POST  | `/logout`    | Выход из системы                  | Да                       |
| GET   | `/me`        | Информация о текущем пользователе | Да                       |

### 🔗 Работа с ссылками

| Метод | Эндпоинт                  | Описание                          | Требуется аутентификация |
|-------|---------------------------|-----------------------------------|--------------------------|
| POST  | `/links/shorten`          | Создание короткой ссылки          | Опционально              |
| GET   | `/{short_code}`           | Перенаправление по короткой ссылке| Нет                      |
| GET   | `/links/search`           | Поиск ссылок по оригинальному URL | Нет                      |
| GET   | `/links/{short_code}/stats`| Статистика по ссылке              | Нет                      |
| DELETE| `/links/{short_code}`     | Удаление ссылки                   | Да (только создатель)    |
| PUT   | `/links/{short_code}`     | Обновление ссылки                 | Да (только создатель)    |
| GET   | `/links/expired`          | Список истекших ссылок            | Нет                      |

## 💡 Примеры использования

### Регистрация пользователя
```bash
curl -X POST "http://localhost:8000/register" \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
```

### Создание короткой ссылки
```bash
curl -X POST "http://localhost:8000/links/shorten" \
  -H "Content-Type: application/json" \
  -d '{
    "original_url": "https://example.com/long/url/path",
    "custom_alias": "my-link",
    "expires_at": "2023-12-31T23:59:59"
  }'
```

### Получение статистики использования ссылки
```bash
curl "http://localhost:8000/links/my-link/stats"
```

## 🛠 Установка и запуск
```bash
Copy
# 1. Клонируйте репозиторий
git clone [https://github.com/yourusername/url-shortener.git](https://github.com/yanaverina/FastAPI_project.git)
cd url-shortener

# 2. Создайте файл .env
cat > .env <<EOL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=urlshortener
REDIS_URL=redis://redis:6379
EOL

# 3. Запустите сервисы через Docker Compose
docker-compose up -d --build

# 4. Проверьте работу API
curl http://localhost:8000
```

После запуска API будет доступно по адресу:
🌐 http://localhost:8000

# 🗃 Структура базы данных

## 📌 Таблица `users`

| Столбец         | Тип данных       | Ограничения               | Описание                |
|-----------------|------------------|---------------------------|-------------------------|
| `id`            | `SERIAL`         | `PRIMARY KEY`             | Уникальный идентификатор|
| `email`         | `TEXT`           | `UNIQUE NOT NULL`         | Email пользователя      |
| `password_hash` | `TEXT`           | `NOT NULL`                | Хеш пароля (bcrypt)     |
| `created_at`    | `TIMESTAMP`      | `DEFAULT CURRENT_TIMESTAMP`| Дата регистрации        |

## 📌 Таблица `links`

| Столбец         | Тип данных       | Ограничения               | Описание                     |
|-----------------|------------------|---------------------------|------------------------------|
| `id`            | `SERIAL`         | `PRIMARY KEY`             | Уникальный идентификатор     |
| `original_url`  | `TEXT`           | `NOT NULL`                | Полный URL для сокращения    |
| `short_code`    | `TEXT`           | `UNIQUE NOT NULL`         | Генерируемый короткий код (6 символов)|
| `custom_alias`  | `TEXT`           | `NULL`                    | Пользовательский алиас (если указан)|
| `expires_at`    | `TIMESTAMP`      | `NULL`                    | Дата истечения срока действия|
| `created_at`    | `TIMESTAMP`      | `DEFAULT CURRENT_TIMESTAMP`| Дата создания ссылки         |
| `clicks`        | `INTEGER`        | `DEFAULT 0`               | Счетчик переходов           |
| `user_id`       | `INTEGER`        | `REFERENCES users(id) ON DELETE SET NULL`| Связь с владельцем ссылки|

## 🔍 Подтверждение запущенного образа
![Screenshot from 2025-03-29 16-48-06](https://github.com/user-attachments/assets/5889bcb8-4623-4d69-a2ed-76b31a77f8bc)

