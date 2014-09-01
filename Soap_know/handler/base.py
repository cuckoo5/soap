#coding=utf-8

import tornado

import session
import util.config as config

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        print 'bbbbbbbbbbbbbbbbbbbbbbbb'
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = session.Session(self.application.session_manager, self)
     
    def get_current_user(self):
        user = self.session.get("user")
#         user = self.get_secure_cookie("user")
        if user:
            user_json = tornado.escape.json_decode(user)
            print 'user = ', user_json
            return user_json
        else:
            return None

    def result(self, code, msg, result):
        ret = self.format(code, msg, result)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(ret)

    def set_current_user(self, user):
#         self.set_secure_cookie("user", tornado.escape.json_encode(user))
        self.session["user"] = tornado.escape.json_encode(user)
        self.session.save()
    
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
        print 'write_error = ', status_code
        if status_code == 404:
            self.render('404.html', title=config.title)
        elif status_code == 500:
            self.render('500.html', title=config.title)
        else:
            super(BaseHandler, self).write_error(status_code, **kwargs)
    
    def format(self, error_code=0, error_msg=None, result=None):
        ret = {"errorCode":error_code, "errorMessage":error_msg, "result":result}
        return tornado.escape.json_encode(ret)