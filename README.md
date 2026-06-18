# Site Monitor

Скрипт для мониторинга доступности сайтов. Проверяет список URL и записывает результаты в лог файл.

## Требования

- Docker
- Docker Compose

## Быстрый старт

Клонируй репозиторий:

```bash
git clone https://github.com/tiltimmy/site-monitor.git
cd site-monitor
```

Создай файл `.env` в папке проекта:

```
API_URL=https://open.er-api.com/v6/latest/RUB
```

Запусти через Docker Compose:

```bash
docker compose up
```

## Результат

После запуска в терминале увидишь статус каждого сайта:

```
https://google.com доступен.
https://github.com доступен.
https://hvdhvfjfjf.com недоступен.
```

Результаты также записываются в `log.txt`.

## CI/CD

Проект использует GitHub Actions для автоматического деплоя:

1. При каждом push в `main` запускаются тесты
2. Собирается Docker образ и пушится в Docker Hub
3. Сервер автоматически скачивает новый образ и перезапускает контейнер

## Технологии

- Python 3.11
- Docker
- Docker Compose
- GitHub Actions
