#coding=utf-8

from tornado import gen

import tornado.web
import util.config as config
import util.constants as constants

from oauth.baidu import BaiduMixin
from oauth.douban import DoubanMixin
from oauth.qq import QQMixin
from oauth.weibo import WeiboMixin
from db.manager import UserManager
from handler.base import BaseHandler

class LoginHandler(BaseHandler):
    def initialize(self):
        self.user_manager = UserManager()
    
    def get(self):
        print 'login handler'
        if self.get_current_user():
            self.redirect('/')
            return
        else:
            self.render("auth/login.html", title=config.title)
 
    def post(self):
        if self.get_current_user():
            raise tornado.web.HTTPError(403)
        
        user_name = self.get_argument("username", "")
        password = self.get_argument("password", "")
        user = self.user_manager.check_auth(user_name, password)
        if user:
            self.set_current_user(user)
            result = {"token" : self.session.session_id}
#             next = self.get_argument('next', '/')
#             print 'next = ', next
#             self.redirect(self.get_argument('next', '/'))
            self.format(constants.STATUS_CODE_OK, None, result)
        else:
            self.format(constants.STATUS_CODE_NOT_REGISTER, None, None)
#         user = self.application.syncdb['users'].find_one({'user': user_name})
#  
#         # Warning bcrypt will block IO loop:
#         if user and user['password'] and bcrypt.hashpw(password, user['password']) == user['password']:
#             self.set_current_user(user_name)
#             self.redirect("/")
#         else:
#             self.set_secure_cookie('flash', "Login incorrect")
#             self.redirect(u"/login")

class QQAuthLoginHandler(BaseHandler, QQMixin):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        if self.get_argument('code', None):
            user = yield self.get_authenticated_user(
                redirect_uri='YOUR_REDIRECT_URI',
                client_id='qq_api_key',
                client_secret='qq_api_secret',
                code=self.get_argument('code')
            )
            self.render('qq.html', user=user)
        else:
            self.authorize_redirect(
                redirect_uri='YOUR_REDIRECT_URI',
                client_id='qq_api_key',
            )

class BaiduAuthLoginHandler(BaseHandler, BaiduMixin):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        if self.get_argument('code', None):
            user = yield self.get_authenticated_user(
                redirect_uri='YOUR_REDIRECT_URI',
                client_id='baidu_api_key',
                client_secret='baidu_api_secret',
                code=self.get_argument('code')
            )
            self.render('main.html', user=user)
        else:
            self.authorize_redirect(
                redirect_uri="YOUR_REDIRECT_URI",
                client_id='baidu_api_key'
            )

class DoubanAuthLoginHandler(BaseHandler, DoubanMixin):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        if self.get_argument('code', None):
            user = yield self.get_authenticated_user(
                redirect_uri='YOUR_REDIRECT_URI',
                client_id='douban_api_key',
                client_secret='douban_api_secret',
                code=self.get_argument('code')
            )
            self.render('douban.html', user=user)
        else:
            self.authorize_redirect(
                redirect_uri='YOUR_REDIRECT_URI',
                client_id='douban_api_key'
            )

class WeiboAuthLoginHandler(BaseHandler, WeiboMixin):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        if self.get_argument('code', None):
            user = yield self.get_authenticated_user(
                redirect_uri='YOUR_REDIRECT_URI',
                client_id='weibo_api_key',
                client_secret='weibo_api_secret',
                code=self.get_argument('code')
            )
            self.render('weibo.html', user=user)
        else:
            self.authorize_redirect(
                redirect_uri='YOUR_REDIRECT_URI',
                client_id='weibo_api_key'
            )

class LogoutHandler(BaseHandler):
    def get(self):
        self.session.clear()
        self.redirect("/")

class RegisterHandler(LoginHandler):
    def initialize(self):
        self.user_manager = UserManager()
    
    def get(self):
        self.post()
#         self.render("auth/register.html", title=config.title)
 
    def post(self):
        print 'register handler'
        user_name = self.get_argument("username", "")
        email = self.get_argument("email", "")
        password = self.get_argument("password", "")
        
        user = self.user_manager.get_user(user_name, email)
        if user:
            error_msg = u"?error=" + tornado.escape.url_escape("Login name already taken")
            self.redirect(u"/login" + error_msg)
 
        user = {}
        user['user_name'] = user_name
        user['email'] = email
        user['password'] = password
        success = self.user_manager.create_user(user)
        if success :
#             self.redirect(self.get_argument('next', '/login'))
            self.format(constants.STATUS_CODE_OK, None, None)