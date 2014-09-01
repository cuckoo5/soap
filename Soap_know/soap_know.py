#coding=utf-8

# from bson.objectid import ObjectId
# from tornado import gen

import os.path
import tornado.web

import session
import util.config as config

# from auth.auth import BaiduMixin, DoubanMixin, QQMixin, WeiboMixin
from handler.about import AboutHandler
from handler.auth import LoginHandler, LogoutHandler, RegisterHandler
from handler.channel import ChannelHandler
from handler.community import CommunityHandler
from handler.error import PageNotFoundHandler
from handler.formula import FormulaHandler
from handler.market import MarketHandler
from handler.main import MainHandler
from handler.user import UserHandler

class Application(tornado.web.Application): 
    def __init__(self):
        print 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "html"),
            "cookie_secret" : "e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            "session_secret" : "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
#             "xsrf_cookies" : True,
#             "memcached_address" : ["127.0.0.1:11211"],
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
            (r"/register", RegisterHandler),
            (r".*", PageNotFoundHandler)
        ]
        
        tornado.web.Application.__init__(self, handlers, **settings)
        memcached_address = '%s:%d' %(config.cache_ip, config.cache_port)
        self.session_manager = session.SessionManager(settings["session_secret"], [memcached_address], config.cache_session_timeout)

tornado.web.ErrorHandler = PageNotFoundHandler
