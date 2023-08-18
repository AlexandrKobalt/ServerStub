# ServerStub
A mock server for testing API interactions

## Как использовать?
#### 1. Specify the host and port on which the server will be launched
````json
    "server": {
        "host": "127.0.0.1",
        "port": 8080
    },
````
#### 2. Specify the path, method, and response data
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
#### 3. Run the server
````bash
python3 main.py
````
