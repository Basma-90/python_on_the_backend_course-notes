import tornado.web
import tornado.ioloop

class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World! This is a basic request handler.")

class HomeRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("structure.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", BasicRequestHandler),
        (r"/home", HomeRequestHandler)
    ])
    
    port = 8883
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
