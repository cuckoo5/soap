#coding=utf-8

import tornado.web

import util.config as config

from handler.base import BaseHandler

class CommunityHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, param):
        print "param = %s" %param
        url = "community/%s.html" %param
        cur_user = self.get_current_user()
        self.render(url, title=config.title, cur_user=cur_user)