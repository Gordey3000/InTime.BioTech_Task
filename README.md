```markdown
# Проект "Biotech"
```
Проект "Biotech" представляет собой тестовое задание для компании InTime.BioTech .

### Как запустить проект в контейнерах локально:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/gordey3000/foodgram-project-react.git
```

```
cd foodgram-project-react/infra
```

Установить Docker Desktop на Ваш компьютер и запустить его.

Создать директории infra файл .env и заполнить его своими данными:

```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<your_password>
DB_HOST=foodgram_db
DB_PORT=5432
DEBUG=False
SECRET_KEY=<your_secret_key>
ALLOWED_HOSTS=localhost you_can_add_your_host_here
```

Запустить оркестр контейнеров:

```
docker compose up
```

Дождаться сборки и запуска всех контейнеров и в другом окне терминала выполнить миграции:
```
docker compose exec web-app python manage.py makemigrations
```

```
docker compose exec web-app python manage.py migrate 
```
Проект будет доступен по адресу: http://localhost/

## Использование

### API Endpoints

- `/api/users/`: Получение информации о пользователях.
- `/api/users/me/`: Получение и редактирование информации о текущем пользователе.
- `/auth/signup/`: Регистрация нового пользователя.

### Сериализаторы

#### UsersSerializer

Сериализатор для просмотра пользователей.

Поля:
- username: Имя пользователя.
- email: Адрес электронной почты пользователя.
- first_name: Имя пользователя.
- last_name: Фамилия пользователя.
- bio: Биография пользователя.

#### UserMeSerializer

Сериализатор для просмотра и редактирования информации о текущем пользователе.

Поля:
- username: Имя пользователя.
- email: Адрес электронной почты пользователя.
- first_name: Имя пользователя.
- last_name: Фамилия пользователя.
- bio: Биография пользователя.

#### RegistrationSerializer

Сериализатор для регистрации нового пользователя.

Поля:
- email: Адрес электронной почты пользователя.
- username: Имя пользователя.

### Модель User

Пользовательская модель пользователя.

Поля:
- email: Адрес электронной почты пользователя.
- bio: Биография пользователя.
- first_name: Имя пользователя.
- last_name: Фамилия пользователя.