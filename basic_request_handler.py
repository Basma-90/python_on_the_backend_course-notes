import tornado.web
import tornado.ioloop

class request_handler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    

if __name__ == "__main__":
    app=tornado.web.application([
        (r"/",request_handler),
    ])
    app.listen(8888)
    print("Listening on port 8888")
    tornado.ioloop.IOLoop.current().start()
