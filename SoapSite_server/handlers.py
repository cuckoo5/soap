#coding=utf-8
'''
Created on 2013-11-25

@author: cuckoo5
'''

from bson.objectid import ObjectId
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
        infos = []
        self.render("index.html", title=TITLE)

class OilHandler(BaseHandler):
    def get(self, oil_type):
        print "oil type = %s" %oil_type
        oil_url = "oil/%s.html" %oil_type
        self.render(oil_url, title=TITLE)

class FormulaHandler(BaseHandler):
    def get(self, formula_type):
        print "formula type = %s" %formula_type
        formula_url = "formula/%s.html" %formula_type
        
        if formula_type == "difficulty":
            self.render(formula_url, title=TITLE, difficulty_level=datas.difficulty_level)
        elif formula_type == "efficacy":
            pass
        elif formula_type == "function":
            pass
        elif formula_type == "skin":
            skins = []
            skin_types = db.query(init_datas.tb_skin_type)
            print 'type = ', type(skin_types)
#             count = skin_types.count()
            for skin in skin_types:
                print '---------------------------'
                print 'skin = ', skin
                formulas = []
                for formula in datas.formulas:
                    formula_skin_type = formula['skin_types']
                    print "skin = ", skin['_id']
                    print "formula_skin_type = ", formula_skin_type
                    if skin['_id'] in formula_skin_type:
                        formulas.append(formula)
                print formulas
                skin['formulas'] = formulas
                skins.append(skin)
            self.render(formula_url, title=TITLE, skin_types=skin_types)

class ForumHandler(BaseHandler):
    def get(self):
        pass