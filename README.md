## Тестовое задание
### Задеплоенный вариант  
Beget: 1cpu 1ram
1. http://31.128.46.67

### Локальный запуск  
1. В папке `project` добавить `.env` файл и заполнить его в соответствии с `config.py`  
2. В папке `docker` поднимаем контейнеры через прод-версию compose-файла:  
```bash
docker compose -f docker/docker-compose-prod.yml up -d
```  
3. Готово
