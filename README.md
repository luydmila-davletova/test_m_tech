# Web api сервис
## Стек
Python 3.11, FastAPI, Alembic, uvicorn, pydantic

## Описание
Сервис принимает на вход строку вида :
```
'IP HTTP-метод URI status-code'
```

Парсит ее в делает запись в базу данных, присваивая ей уникальный идентификатор и дату создания записи

## **Как запустить проект**:
* Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/luydmila-davletova/test_m_tech
```
* Создать и активировать виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```
* Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```
* Создание БД.
```
alembic upgrade head
```
* Наполнение env-файла.
```
DATABASE_URL= sqlite+aiosqlite:///./fastapi.db
LOG_GENERATOR_N = {любое число}
LOG_GENERATOR_M = {любое число}
```
* Стандартный запуск:
```
uvicorn app.main:app
```
* Запуск сервера с автоматическим перезапуском при изменении кода (только для режима разработки):
```
uvicorn app.main:app --reload
```
Сервер будет доступен локально по адресу: http://127.0.0.1:8000

Документация будет доступна по адресу:
http://127.0.0.1:8000/docs/