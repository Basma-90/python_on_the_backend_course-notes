import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import json

class MainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", 'r')
        todo_list = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(todo_list))
    
    def post(self):
        item = self.get_argument('item')
        fh = open("list.txt", 'a')
        fh.write(item + "\n")
        fh.close()
        self.write(json.dumps({"message": "Item added to list"}))
    
    def delete(self):
        item = self.get_argument('item')
        fh = open("list.txt", 'r')
        todo_list = fh.read().splitlines()
        fh.close()
        fh = open("list.txt", 'w')
        for i in todo_list:
            if i != item:
                fh.write(i + "\n")
        fh.close()
        self.write(json.dumps({"message": "Item removed from list"}))

    def put(self):
        item = self.get_argument('item')
        new_item = self.get_argument('new_item')
        fh = open("list.txt", 'r')
        todo_list = fh.read().splitlines()
        fh.close()
        fh = open("list.txt", 'w')
        for i in todo_list:
            if i == item:
                fh.write(new_item + "\n")
            else:
                fh.write(i + "\n")
        fh.close()
        self.write(json.dumps({"message": "Item updated in list"}))


if __name__ == "__main__":  
    app = tornado.web.Application([
        (r"/", MainRequestHandler),
        (r"/list", ListRequestHandler),
    ])
    port = 8882
    app.listen(port)
    print("Listening on port:", port)
    tornado.ioloop.IOLoop.current().start()
