# coding=utf-8

from tornado import httpclient

from tornado.auth import OAuth2Mixin

class BaseMixin(OAuth2Mixin):
    def get_auth_http_client(self):
        return httpclient.AsyncHTTPClient()
