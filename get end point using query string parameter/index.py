import tornado.web
import tornado.ioloop
import tornado.httpserver

class query_param_request_handler(tornado.web.RequestHandler):
    def get(self):
        # Get the query parameters
        param1 = self.get_argument('param1')
        if(param1.isdigit()):
            r="odd" if param1%2 else "even"
            self.write(f"the number {param1} is {r}")
        else:
            self.write(f"the number {param1} is not a number")
#localhost:8888/isEven?param1=5

class resource_param_request_handler(tornado.web.RequestHandler):
        def get(self, name, id):
            self.write(f"Hello {name} with id {id}")
#localhost:8888/students/Hussein/1234



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/isEven", query_param_request_handler),
        (r"/student/([a-z]+)/(0-9)+", resource_param_request_handler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()

