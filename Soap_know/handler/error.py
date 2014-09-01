#coding=utf-8

import tornado.web

from handler.base import BaseHandler

class PageNotFoundHandler(BaseHandler):
    def get(self):
        raise tornado.web.HTTPError(404)