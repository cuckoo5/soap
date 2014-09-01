#coding=utf-8

import tornado.web

import util.config as config

from handler.base import BaseHandler

class MainHandler(BaseHandler):
    def get(self):
        print 'main handler'
        cur_user = self.get_current_user()
        self.render("index.html", title=config.title, cur_user=cur_user)
