#coding=utf-8
'''
Created on 2013-11-21

@author: cuckoo5
'''
import logging
import tornado.auth
import tornado.escape
import tornado.ioloop
import tornado.web
import os.path
import uuid

from tornado import gen
from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class FormulaHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("formula")

application = tornado.web.Application([
    (r"/", MainHandler),
])

def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/auth/login", FormulaHandler)
            ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        login_url="/auth/login",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        )
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()