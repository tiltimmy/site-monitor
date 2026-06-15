# Site Monitor

Python скрипт для мониторинга доступности сайтов.

## Что умеет
- Проверяет список сайтов
- Записывает результаты в лог файл
- Запускается в Docker контейнере

## Запуск через Docker
```bash
docker build -t monitor .
docker run -v $(pwd):/app monitor
```

## Технологии
- Python 3.11
- Docker
- Docker Compose

