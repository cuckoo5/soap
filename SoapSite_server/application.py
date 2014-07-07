#coding=utf-8
'''
Created on 2013-11-25

@author: cuckoo5
'''

import os.path
import tornado.web

from handlers import MainHandler, FormulaHandler, ForumHandler, OilHandler

class Application(tornado.web.Application): 
    def __init__(self):
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "html"),
        }
        handlers = [
            (r"/", MainHandler),
            (r"/oil/(\w+)", OilHandler),
            (r"/formula/(\w+)", FormulaHandler),
            (r"/forum/(\w+)", ForumHandler)
        ]
        
        tornado.web.Application.__init__(self, handlers, **settings)
