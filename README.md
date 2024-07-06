 # JobHunter

   Описание

 JobHunter - это Django-приложение для парсинга вакансий с hh.ru.

## Установка

 1. Клонируйте репозиторий
git clone https://github.com/yourusername/JobHunter.git
cd JobHunter

2.Настройка виртуального окружения
python3 -m venv venv
source venv/bin/activate

3. Установка зависимостей
pip install -r requirements.txt
pip install psycopg2-binary

5. Настройка базы данных

Установите PostgreSQL, если еще не установлено:
sudo apt update
sudo apt install postgresql postgresql-contrib

Запустите и включите сервис PostgreSQL:
sudo systemctl start postgresql
sudo systemctl enable postgresql

Создайте базу данных и пользователя:
sudo -i -u postgres
psql
CREATE DATABASE jobhunterdb;
CREATE USER jobuser WITH PASSWORD 'jobpassword';
GRANT ALL PRIVILEGES ON DATABASE jobhunterdb TO jobuser;
\q
exit

Проверьте подключение к базе данных:
psql -h localhost -d jobhunterdb -U jobuser

5. Настройка Django
Примените миграции:
python manage.py makemigrations
python manage.py migrate

Создайте суперпользователя:
python manage.py createsuperuser

Запустите сервер:
python manage.py runserver

## Запуск с Docker
Создайте Dockerfile и docker-compose.yml.

Запустите проект:
docker-compose up --build

Использование API
Получение списка вакансий
curl -X GET http://localhost:8000/api/vacancies/

Получение списка кандидатов
curl -X GET http://localhost:8000/api/candidates/

Создание новой вакансии
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Vacancy", "description": "Job description"}' http://localhost:8000/api/vacancies/

Создание нового кандидата
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}' http://localhost:8000/api/candidates/

Дополнительные команды
Применение миграций:
python manage.py makemigrations
python manage.py migrate

Создание суперпользователя:
python manage.py createsuperuser

Запуск сервера:
python manage.py runserver

Запуск тестов:
python manage.py test
go



