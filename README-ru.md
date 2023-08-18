# ServerStub
Сервер-заглушка для тестирования взаимодействия с API

## Как использовать?
#### 1. Укажите хост и порт на котором будет запущен сервер
````json
    "server": {
        "host": "127.0.0.1",
        "port": 8080
    },
````
#### 2. Укажите путь, метод и возвращаемые данные
````json
    "endpoints": [
        {
            "path": "/photo",
            "method": "GET",
            "response": "Here is your photo"
        },
        {
            "path": "/data",
            "method": "POST",
            "response": {
                "error": false,
                "message": "",
                "DATA": {},
                "warning": ""
            }
        }
    ]
````
#### 3. Запустите сервер
````bash
python3 main.py
````
