# ToDoManager

ToDoManager — учебный Django-проект для управления задачами.

Проект создан в рамках изучения backend-разработки на Python и Django.
Главная цель проекта — изучить базовую архитектуру Django-приложений: модели, маршруты, представления, шаблоны, формы, авторизацию, работу с базой данных и подготовку проекта к деплою.

---

## Возможности проекта

* Регистрация пользователей
* Авторизация пользователей
* Выход из аккаунта
* Создание задач
* Просмотр списка задач
* Редактирование задач
* Удаление задач
* Привязка задач к конкретному пользователю
* Защита страниц от неавторизованных пользователей
* Запрет доступа к чужим задачам
* Поиск задач по названию и описанию
* Фильтрация задач по статусу
* Сортировка задач
* Уведомления после создания, редактирования и удаления задач
* Админ-панель Django
* Подключение PostgreSQL
* Использование переменных окружения через `.env`
* Подготовка static-файлов через WhiteNoise
* Production-запуск через Gunicorn

---

## Технологии

* Python
* Django
* PostgreSQL
* HTML
* Bootstrap
* Django ORM
* Django Templates
* Django Forms
* Class-Based Views
* Git
* GitHub
* WhiteNoise
* Gunicorn
* python-dotenv

---

## Структура проекта

```text
ToDoManager/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   │
│   │   └── tasks/
│   │       ├── includes/
│   │       │   └── task_form.html
│   │       ├── base.html
│   │       ├── task_list.html
│   │       ├── task_create.html
│   │       ├── task_update.html
│   │       └── task_delete.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Procfile
└── README.md
```

---

## Основные страницы

```text
/tasks/                  список задач
/tasks/create/           создание задачи
/tasks/<id>/edit/        редактирование задачи
/tasks/<id>/delete/      удаление задачи
/tasks/register/         регистрация
/accounts/login/         вход
/accounts/logout/        выход
/admin/                  админ-панель
```

---

## Установка и запуск проекта локально

### 1. Клонировать репозиторий

```bash
git clone <your-repository-url>
cd ToDoManager
```

---

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

---

### 3. Активировать виртуальное окружение

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

---

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

---

### 5. Создать файл `.env`

Создай файл `.env` в корне проекта рядом с `manage.py`.

Можно скопировать структуру из файла `.env.example`.

Пример:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

DB_NAME=todomanager_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 6. Создать базу данных PostgreSQL

Создай базу данных PostgreSQL с именем:

```text
todomanager_db
```

Имя базы данных должно совпадать со значением `DB_NAME` в файле `.env`.

---

### 7. Применить миграции

```bash
python manage.py migrate
```

---

### 8. Создать суперпользователя

```bash
python manage.py createsuperuser
```

---

### 9. Запустить сервер разработки

```bash
python manage.py runserver
```

---

### 10. Открыть проект в браузере

```text
http://127.0.0.1:8000/tasks/
```

---

## Переменные окружения

Проект использует файл `.env` для хранения секретных настроек.

Пример переменных:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000,http://localhost:8000

DB_NAME=todomanager_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

Файл `.env` не должен попадать в GitHub.

Для примера используется файл:

```text
.env.example
```

---

## Работа со static-файлами

Для сборки static-файлов используется команда:

```bash
python manage.py collectstatic
```

Собранные static-файлы попадают в папку:

```text
staticfiles/
```

В проекте используется WhiteNoise для раздачи static-файлов в production-режиме.

---

## Production-запуск

Для production-запуска используется Gunicorn.

Команда запуска:

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

Также в проекте есть `Procfile`:

```text
web: gunicorn config.wsgi:application
```

Перед production-запуском нужно выполнить:

```bash
python manage.py migrate
python manage.py collectstatic
```

---

## Проверка проекта

Базовая проверка Django-проекта:

```bash
python manage.py check
```

Проверка перед деплоем:

```bash
python manage.py check --deploy
```

---

## Основные архитектурные решения

### Модель Task

Задача хранит:

* владельца задачи;
* название;
* описание;
* статус выполнения;
* дату создания;
* дату обновления.

Каждая задача связана с пользователем через `ForeignKey`.

---

### Пользователи и доступ

В проекте используется встроенная система пользователей Django.

Доступ к задачам имеют только авторизованные пользователи.

Каждый пользователь видит только свои задачи.

Редактирование и удаление чужих задач запрещено на уровне queryset.

---

### Формы

Для создания и редактирования задач используется `ModelForm`.

Форма вынесена в файл:

```text
tasks/forms.py
```

HTML-код формы вынесен в отдельный partial-шаблон:

```text
tasks/templates/tasks/includes/task_form.html
```

---

### Class-Based Views

CRUD задач реализован через generic class-based views:

* `ListView`
* `CreateView`
* `UpdateView`
* `DeleteView`

Для ограничения доступа используется `LoginRequiredMixin`.

Для ограничения queryset задач текущим пользователем используется собственный mixin.

---

### QuerySet и Manager

В модели задач используется кастомный `TaskQuerySet`.

Он содержит методы:

* `for_user()`
* `completed()`
* `active()`
* `search()`

Это позволяет писать более читаемые ORM-запросы.

---

## Полезные команды

Создать приложение:

```bash
python manage.py startapp tasks
```

Создать миграции:

```bash
python manage.py makemigrations
```

Применить миграции:

```bash
python manage.py migrate
```

Создать суперпользователя:

```bash
python manage.py createsuperuser
```

Запустить сервер:

```bash
python manage.py runserver
```

Открыть Django shell:

```bash
python manage.py shell
```

Собрать static-файлы:

```bash
python manage.py collectstatic
```

Проверить проект:

```bash
python manage.py check
```

---

## Что изучено в проекте

В ходе разработки проекта были изучены:

* структура Django-проекта;
* создание приложений;
* работа с `urls.py`;
* function-based views;
* class-based views;
* generic views;
* модели Django;
* миграции;
* Django ORM;
* админ-панель;
* шаблоны;
* наследование шаблонов;
* формы;
* `ModelForm`;
* авторизация;
* регистрация;
* защита страниц;
* связь моделей через `ForeignKey`;
* фильтрация и поиск;
* кастомные QuerySet;
* mixins;
* PostgreSQL;
* переменные окружения;
* static-файлы;
* подготовка к деплою;
* Git и GitHub.

---

## Статус проекта

Проект находится в учебной разработке.

Планируемые улучшения:

* вынести пользователей в отдельное приложение `users`;
* добавить пагинацию;
* добавить тесты;
* улучшить дизайн интерфейса;
* добавить смену пароля;
* добавить восстановление пароля;
* добавить дедлайны задач;
* добавить категории задач;
* добавить приоритеты задач;
* выполнить деплой проекта.

---

## Автор

Санжар Адылетов

Учебный проект для подготовки к стажировке Python Backend Developer.
