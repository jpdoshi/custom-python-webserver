from myserver import app, server

host = 'localhost'
port = 8000

app = app(host, port, server)
server.setRoutes(server, {
    '/': '/templates/index.html',
    '/products': '/templates/products.html'
});

if __name__ == '__main__':
    app.init_server()
