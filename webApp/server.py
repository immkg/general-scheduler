import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
from jsontranslator import *
import sys
sys.path.append('/home/melman/sih/class_files')
from interface import *
import json
from pprint import pprint
# from tornado import web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ResultHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class inputDataHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    # def initialize(self):
    #     self.str = "blabla"
      
    def open(self):
        print 'new connection'
        # self.write_message("tada!")
      
    def on_message(self, message):
        print message
        if(message == "knock"):
            self.write_message("yes")

        else:
            self.write_message("solving..")
            const_dict = conditionInput(message)
            pprint(const_dict)
            ttable = interface(const_dict)
            # ttable = [['Day 0', [], [], [], [], [], []], ['Day 1', [(1, 0, 0, 2), (1, 0, 1, 2)], [(1, 0, 1, 2), (1, 0, 0, 2)], [(1, 0, 1, 2), (1, 0, 0, 2)], [(1, 0, 1, 2), (1, 0, 0, 2)], [], []], ['Day 2', [], [], [(1, 1, 1, 2), (1, 1, 0, 2)], [(1, 1, 0, 2), (1, 1, 1, 2)], [(1, 1, 1, 2), (1, 1, 0, 2)], [(1, 1, 1, 2), (1, 1, 0, 2)]], ['Day 3', [], [], [(0, 0, 1, 2)], [(0, 0, 1, 2)], [(0, 0, 1, 2)], [(0, 0, 1, 2)]], ['Day 4', [], [], [(0, 1, 1, 2), (0, 1, 0, 2)], [(0, 1, 1, 2), (0, 1, 0, 2)], [(0, 1, 0, 2), (0, 1, 1, 2)], [(0, 1, 1, 2), (0, 1, 0, 2)]], ['Day 5', [(0, 0, 0, 1)], [(0, 0, 0, 1)], [(0, 0, 0, 1)], [(0, 0, 0, 1)], [], []]]
            self.write_message(json.dumps(ttable))
            #call the solver
      
    def on_close(self):
        print 'connection closed'
  
if __name__ == '__main__':
  
    application = tornado.web.Application([
    (r'/ws', inputDataHandler),
    (r'/', IndexHandler),
    (r'/result', ResultHandler),
    ])
      
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
