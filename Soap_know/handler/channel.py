#coding=utf-8

import tornado.web

import util.config as config

from handler.base import BaseHandler

class ChannelHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, param):
        print "param = %s" %param
        url = "channel/%s.html" %param
        cur_user = self.get_current_user()
        self.render(url, title=config.title, cur_user=cur_user)