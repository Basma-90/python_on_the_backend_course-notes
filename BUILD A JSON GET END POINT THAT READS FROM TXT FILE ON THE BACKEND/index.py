import tornado.web
import tornado.ioloop
import tornado.httpserver
import json

class list_request_handler(tornado.web.RequestHandler):
    def get(self):
        fh=open("list.txt","r")
        fruits=fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))
    def post(self):
        fh=open("list.txt","a")
        fruit=self.get_argument("fruit")
        fh.write(fruit+"\n")
        fh.close()
        self.write(json.dumps({"status":"ok"}))

#localhost:8888/list?friut=apple


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/list", list_request_handler),
    ])
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
