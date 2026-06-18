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

Запусти через Docker Compose:

```bash
docker compose up
```

## Переменные окружения

Перед запуском установи переменную окружения:

```bash
export API_URL="https://open.er-api.com/v6/latest/RUB"
```

Или передай напрямую при запуске:

```bash
docker run -e API_URL="https://open.er-api.com/v6/latest/RUB" monitor
```

## Результат

После запуска в терминале увидишь статус каждого сайта:

```
https://google.com доступен.
https://github.com доступен.
https://hvdhvfjfjf.com недоступен.
```

Результаты также записываются в `log.txt`.

## Технологии

- Python 3.11
- Docker
- Docker Compose
