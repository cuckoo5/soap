#coding=utf-8
'''
Created on 2013-11-25

@author: cuckoo5
'''

import os.path
import tornado.web

from handlers import MainHandler, AboutHandler, ChannelHandler, CommunityHandler, FormulaHandler, LoginHandler, LogoutHandler, RegisterHandler, MarketHandler, UserHandler

class Application(tornado.web.Application): 
    def __init__(self):
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "html"),
            "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=", # 安全cookie所需的
            "login_url": "/login", # 默认的登陆页面
        }

        handlers = [
            (r"/", MainHandler),
            (r"/about/(\w+)", AboutHandler),
            (r"/channel/(\w+)", ChannelHandler),
            (r"/community/(\w+)", CommunityHandler),
            (r"/formula/(\w+)", FormulaHandler),
            (r"/market/(\w+)", MarketHandler),
            (r"/user/(\w+)", UserHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
            (r"/register", RegisterHandler)
        ]
        
        tornado.web.Application.__init__(self, handlers, **settings)
