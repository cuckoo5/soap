#coding=utf-8

from pymongo import MongoClient

import db_config as config
import mongo_init_datas as init_all_datas

class MongoDB:

    def __init__(self):
        self.db = self.get_connect()
        
    def get_connect(self):
        client = MongoClient(config.uri, config.port)
        #client = MongoClient('mongodb://localhost:27017/')
        db = client[config.db_name]
        return db

    def tables(self):
        print self.db.collection_names()

    def query(self, tb_name, condition=None):
        results = []
        datas = self.db[tb_name].find(condition)
        for data in datas:
            result = data
            result['_id'] = str(data['_id'])
            results.append(result)
        return results
    
    def count(self, tb_name, condition=None):
        cursor = self.db[tb_name].find(condition)
        count = cursor.count()
        return count
    
    def insert(self, tb_name, datas):
        if (datas):
            self.db[tb_name].insert(datas)
    
    def delete(self, tb_name, condition):
        self.db[tb_name].remove(condition)
    
    def update(self, tb_name, datas):
        if (datas):
            table = self.db[tb_name]
            for d in datas:
                table.update({'_id':d['_id']}, d, True)
    
if __name__ == '__main__':
    mongo = MongoDB()
    mongo.tables()
    mongo.query(init_all_datas.tb_formula_type)
    mongo.query(init_all_datas.tb_skin_type)

