#coding=utf-8

import hashlib
from db.mysql_db import MySQLDB

db = MySQLDB()

class UserManager:
    def __init__(self):
        pass
    
    def check_auth(self, user_name, password):
        user = None
        password_md5 = hashlib.md5(password).hexdigest()
        print 'password_md5 = ', password_md5
        sql = "select id, user_name, email from user where user_name = %s and password = %s "
        result = db.query(sql, user_name, password_md5)
        if (result and len(result) > 0):
            user = result[0]
#             item = result[0]
#             user['id'] = item[0]
#             user['user_name'] = item[1]
#             user['email'] = item[2]
        return user
    
    def get_user(self, user_name, email):
        user = {}
        sql = "select id, user_name, email from user where user_name = %s or email = %s "
        result = db.query(sql, user_name, email)
        if (result and len(result) > 0):
            user = result[0]
#             item = result[0]
#             user['id'] = item[0]
#             user['user_name'] = item[1]
#             user['email'] = item[2]
        return user
    
    def create_user(self, user):
        success = True
        password_md5 = hashlib.md5(user['password']).hexdigest()
        
        sql = "insert into user (user_name, email, password) values (%s, %s, %s)"
        db.insert(sql, user['user_name'], user['email'], password_md5)
        return success

class FormulaManager:
    def __init__(self):
        pass

    def get_all_skin_types(self):
        sql = "select * from skin_type"
        result = db.query(sql)
        return result
#         skin_types = []
#         for item in result:
#             skin = {}
#             skin['id'] = item[0]
#             skin['name'] = item[1]
#             skin['description'] = item[2]
#             skin_types.append(skin)
#         return skin_types
    
    def get_formulas(self, skin_type=None, difficult_degree=None, use=None):
        formulas = [
            {'name' : 'aaa', 'use' : '10%', 'skin_types' : 'bbb', 'difficult_degree' : 'ccc', 'efficacy' : 'ddd'},
            {'name' : 'aaa', 'use' : '10%', 'skin_types' : 'bbb', 'difficult_degree' : 'ccc', 'efficacy' : 'ddd'},
            {'name' : 'aaa', 'use' : '10%', 'skin_types' : 'bbb', 'difficult_degree' : 'ccc', 'efficacy' : 'ddd'},
            {'name' : 'aaa', 'use' : '10%', 'skin_types' : 'bbb', 'difficult_degree' : 'ccc', 'efficacy' : 'ddd'},
            {'name' : 'aaa', 'use' : '10%', 'skin_types' : 'bbb', 'difficult_degree' : 'ccc', 'efficacy' : 'ddd'}
        ]
        return formulas

class OilManager:
    def __init__(self):
        pass
    
    def get_oils(self):
        sql = '''select name, name_en, describ, naoh, koh, min_usage, max_usage, ins, price from oil'''
        result = db.query(sql)
        oils = []
        for item in result:
            oil = item
            min_usage = item['min_usage']
            max_usage = item['max_usage']
            if (min_usage == max_usage):
                if max_usage == 0:
                    oil['suggested_usage'] = ''
                elif (max_usage > 0 and max_usage <= 100):
                    min_usage = 0
                    oil['min_usage'] = 0
                    oil['suggested_usage'] = '%d%%-%d%%' %(min_usage, max_usage)
            else:
                oil['suggested_usage'] = '%d%%-%d%%' %(min_usage, max_usage)
            oils.append(oil)
        return oils
#         oils = [
#             {'name' : 'aaa', 'suggested_usage' : '10%', 'naoh' : 'bbb', 'koh' : 'ccc', 'ins' : 'ddd', 'price' : 10.0},
#             {'name' : 'aaa', 'suggested_usage' : '10%', 'naoh' : 'bbb', 'koh' : 'ccc', 'ins' : 'ddd', 'price' : 10.0},
#             {'name' : 'aaa', 'suggested_usage' : '10%', 'naoh' : 'bbb', 'koh' : 'ccc', 'ins' : 'ddd', 'price' : 10.0},
#             {'name' : 'aaa', 'suggested_usage' : '10%', 'naoh' : 'bbb', 'koh' : 'ccc', 'ins' : 'ddd', 'price' : 10.0},
#             {'name' : 'aaa', 'suggested_usage' : '10%', 'naoh' : 'bbb', 'koh' : 'ccc', 'ins' : 'ddd', 'price' : 10.0}
#         ]
#         return oils
