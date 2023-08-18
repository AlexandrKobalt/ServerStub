import http.server
import json

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request("GET")

    def do_POST(self):
        self.handle_request("POST")

    def do_PUT(self):
        self.handle_request("PUT")

    def do_DELETE(self):
        self.handle_request("DELETE")

    def handle_request(self, method):
        with open('config.json') as config_file:
            config = json.load(config_file)

        path = self.path
        response = None

        for endpoint in config.get("endpoints", []):
            if endpoint["path"] == path and endpoint["method"] == method:
                response = endpoint["response"]
                break

        if response is None:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                "error": True,
                "message": "Endpoint not found"
            }
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

        response_json = json.dumps(response)
        self.wfile.write(response_json.encode('utf-8'))

def main():
    with open('config.json') as config_file:
        config = json.load(config_file)

    host = config.get("host", "127.0.0.1")
    port = config.get("port", 8080)

    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)

    print(f"Server running on {host}:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
