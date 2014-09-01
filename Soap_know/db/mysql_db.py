# coding=utf-8

import torndb

import util.config as config

class MySQLDB:
    def __init__(self):
        self.connect = self.get_connect()
    
    def get_connect(self):
        ip = config.db_ip
        port = config.db_port
        db_name = config.db_name
        user_name = config.db_user_name
        password = config.db_password
#         connect = MySQLdb.Connect(host=ip, user=user_name, passwd=password, port=port, db=db_name, charset='utf8')
        url = '%s:%d' %(ip, port)
        connect = torndb.Connection(url, db_name, user=user_name, password=password)
        return connect
    
    def query(self, sql, *param):
        result = self.connect.query(sql, *param)
        return result
    
    def insert(self, sql, *param):
        self.connect.insert(sql, *param)
    
    def insert_many(self, sql, *param):
        self.connect.insertmany(sql, *param)  
#     def query(self, sql, param=None):
#         try:
#             conn = self.get_connect()
#             cur = conn.cursor()
#             if param :
#                 cur.execute(sql, param)
#             else :
#                 cur.execute(sql) 
#             
#             result = cur.fetchall()
#             conn.commit()
#             cur.close()
#             conn.close()
#             
#             return result
#         except MySQLdb.Error, e:
#             print "MySQL Error %d: %s" % (e.args[0], e.args[1])
    
#     def update(self, sql, param=None):
#         try:
#             conn = self.get_connect()
#             cur = conn.cursor()
#             if param :
#                 cur.execute(sql, param)
#             else :
#                 cur.execute(sql) 
#             
#             conn.commit()
#             cur.close()
#             conn.close()
#         except MySQLdb.Error, e:
#             print "MySQL Error %d: %s" % (e.args[0], e.args[1])
    
if __name__ == '__main__':
    db = MySQLDB()
    sql = "select * from skin_type"
    result = db.query(sql)
    print result
#     skin_types = []
#     for item in result:
#         skin = {}
#         skin['id'] = item[0]
#         skin['name'] = item[1]
#         skin['description'] = item[2]
#         skin_types.append(skin)
#     print skin_types