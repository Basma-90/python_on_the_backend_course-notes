import tornado.ioloop
import tornado.web
import tornado.websocket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files=self.request.files["imgFile"]
        print(f"Received {len(files)} files")
        for f in files:
            fh=open(f"img/{f.filename}","wb")
            fh.write(f.body)
            fh.close()
        self.write(f"img/{f.filename}")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"}),
    ])
    port=8889
    app.listen(port)
    print(f"Server started on port {port}")
    tornado.ioloop.IOLoop.instance().start()