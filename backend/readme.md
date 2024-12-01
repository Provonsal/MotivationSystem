# Установка серверной части

Для работы базы данных необходим docker и docker compose в частности.

* Установить docker, docker compose

В файле docker-compose-local.py Заполнить:

* Имя контейнера (container_name:)
* Имя пользователя (POSTGRES_USER=)
* Пароль пользователя (POSTGRES_PASSWORD=)
* Название базы данных (POSTGRES_DB=)

```bash
# запуск контейнера базы данных
docker compose -f "docker-compose-local.yaml" up -d \

# установка зависимостей питона
python3 -m venv .venv \
source .venv/bin/activate \
pip install -r "requirements.txt" \
python3 main.py
```
