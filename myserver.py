from http.server import SimpleHTTPRequestHandler
from http.server import HTTPServer

class app():
    def __init__(self, host, port, Server):
        self.host = host
        self.port = port
        self.Server = Server

    def init_server(self):
        webServer = HTTPServer((self.host, self.port), self.Server)
        print(f"Service initiated on http://{self.host}:{self.port}")

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("\nService terminated")

class server(SimpleHTTPRequestHandler):
    def setRoutes(self, routes):
        self.routes = routes

    def do_GET(self):
        for r in self.routes:
            if self.path == r:
                self.path = self.routes[r]
        return SimpleHTTPRequestHandler.do_GET(self)
