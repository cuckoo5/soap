#coding=utf-8

import tornado.web

import util.config as config

from handler.base import BaseHandler

class AboutHandler(BaseHandler):
    def get(self, param):
        print 'about handler'
        url = 'about/%s.html' %param
        self.render(url, title=config.title)