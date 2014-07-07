#coding=utf-8
'''
Created on 2013-11-25

@author: cuckoo5
'''

from bson.objectid import ObjectId
# import bcrypt
import urlparse
import tornado.web

from db.mongo_db import MongoDB
import db.mongo_init_datas as init_datas
import datas

TITLE = "Know"
db = MongoDB()

class BaseHandler(tornado.web.RequestHandler):
    
#     def __init__(self):
#         print '---------------------------------base handler'
#         self.db = MongoDB()
#     def get_login_url(self):
#         return u"/login"
     
    def get_current_user(self):
        user_json = self.get_secure_cookie("user")
        if user_json:
#             return tornado.escape.json_decode(user_json)
            return user_json
        else:
            return None
            
    def set_current_user(self, user):
        self.set_secure_cookie("user", user)
#     # Allows us to get the previous URL
#     def get_referring_url(self):
#         try:
#             _, _, referer, _, _, _ = urlparse.urlparse(self.request.headers.get('Referer'))
#             if referer:
#                 return referer
#         # Test code will throw this if there was no 'previous' page
#         except AttributeError:
#             pass
#         return '/'
# 
#     def get_flash(self):
#         flash = self.get_secure_cookie('flash')
#         self.clear_cookie('flash')
#         return flash
# 
#     def get_essentials(self):
#         mp = {k: ''.join(v) for k, v in self.request.arguments.iteritems()}
#         print mp
#         pass
    
    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
        elif status_code == 500:
            self.render('500.html')
        else:
            self.write("You caused a %d error." % status_code)

class MainHandler(BaseHandler):
    def get(self):
        print 'main handler'
        cur_user = self.get_current_user()
        self.render("index.html", title=TITLE, cur_user=cur_user)

class LoginHandler(BaseHandler):
    def get(self):
        print 'login handler'
        next = self.get_argument("next", "/")
        print 'next = ', next
        self.render("auth/login.html", title=TITLE)
#         self.write('<html><body><form action="/login" method="post">'
#                    'Name: <input type="text" name="name">'
#                    '<input type="submit" value="Sign in">'
#                    '</form></body></html>')
#         messages = self.application.syncdb.messages.find()
#         self.render("login.html", notification=self.get_flash())
 
    def post(self):
        user_name = self.get_argument("username", "")
        password = self.get_argument("password", "")
        print 'user name = ', user_name
        print 'password = ', password
#         user = {'user_name' : user_name, 'password' : password}
#         self.set_current_user(user)
        self.set_current_user(user_name)
        self.redirect("/")
        
#         user = self.application.syncdb['users'].find_one({'user': user_name})
#  
#         # Warning bcrypt will block IO loop:
#         if user and user['password'] and bcrypt.hashpw(password, user['password']) == user['password']:
#             self.set_current_user(user_name)
#             self.redirect("/")
#         else:
#             self.set_secure_cookie('flash', "Login incorrect")
#             self.redirect(u"/login")
 
#     def set_current_user(self, user):
#         print "setting " + user
#         if user:
#             self.set_secure_cookie("user", tornado.escape.json_encode(user))
#         else:
#             self.clear_cookie("user")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/")

class RegisterHandler(LoginHandler):
    def get(self):
        print 'register handler'
        self.render("auth/register.html", title=TITLE)
#         self.render("register.html", next=self.get_argument("next", "/"))
# 
#     def post(self):
#         email = self.get_argument("email", "")
# 
#         already_taken = self.application.syncdb['users'].find_one({'user': email})
#         if already_taken:
#             error_msg = u"?error=" + tornado.escape.url_escape("Login name already taken")
#             self.redirect(u"/login" + error_msg)
# 
#         # Warning bcrypt will block IO loop:
#         password = self.get_argument("password", "")
#         hashed_pass = bcrypt.hashpw(password, bcrypt.gensalt(8))
# 
#         user = {}
#         user['user'] = email
#         user['password'] = hashed_pass
# 
#         auth = self.application.syncdb['users'].save(user)
#         self.set_current_user(email)
# 
#         self.redirect("hello")
        
class ChannelHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, param):
        print "param = %s" %param
        url = "channel/%s.html" %param
        cur_user = self.get_current_user()
        self.render(url, title=TITLE, cur_user=cur_user)

class CommunityHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, param):
        print "param = %s" %param
        url = "community/%s.html" %param
        cur_user = self.get_current_user()
        self.render(url, title=TITLE, cur_user=cur_user)

class FormulaHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, param):
        print "param = %s" %param
        url = 'formula/%s.html' %param
        cur_user = self.get_current_user()
        self.render(url, title=TITLE, cur_user=cur_user)

class MarketHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, param):
        print "param = %s" %param
        url = 'market/%s.html' %param
        cur_user = self.get_current_user()
        self.render(url, title=TITLE, cur_user=cur_user)

class AboutHandler(BaseHandler):
    def get(self, param):
        print 'about handler'
        print "param = %s" %param
        url = 'about/%s.html' %param
        self.render(url, title=TITLE)

class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, param):
        print 'user handler'
        url = 'user/%s.html' %param
        cur_user = self.get_current_user()
        print 'cur_user = ', cur_user
        self.render(url, title=TITLE, cur_user=cur_user)
