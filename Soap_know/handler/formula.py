#coding=utf-8

import tornado.web

import util.config as config
import util.constants as constants

from db.manager import FormulaManager, OilManager
from handler.base import BaseHandler

class FormulaHandler(BaseHandler):
    def initialize(self):
        self.all_use = constants.use
        self.all_difficult_degree = constants.difficult_degree
        self.oil_manager = OilManager()
        self.formula_manager = FormulaManager()
        self.all_skin_types = self.formula_manager.get_all_skin_types()

    @tornado.web.authenticated
    def get(self, param):
        print "param = %s" %param
        url = 'formula/%s.html' %param
        cur_user = self.get_current_user()
        switch = {'index' : self.index, 'new' : self.new}
        switch[param](url, cur_user)
#         self.render(url, title=TITLE, cur_user=cur_user)

    def index(self, url, cur_user):
        skin_type = self.get_argument("skin_type", None)
        use = self.get_argument("use", None)
        difficult_degree = self.get_argument("difficult_degree", None)
        print 'skin_type = ', skin_type
        print 'use = ', use
        print 'difficult_degree = ', difficult_degree
        
        formulas = self.formula_manager.get_formulas()
        self.render(url, title=config.title, cur_user=cur_user, use=self.all_use, skin_types=self.all_skin_types, 
                    difficult_degree=self.all_difficult_degree, formulas=formulas)
        
    def new(self, url, cur_user):
        oils = self.oil_manager.get_oils()
        self.render(url, title=config.title, cur_user=cur_user, oils=oils)
