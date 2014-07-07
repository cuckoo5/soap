#coding=utf-8
'''
Created on 2013-11-25

@author: cuckoo5
'''

import tornado.ioloop

from tornado.options import define, options, parse_command_line
from tornado.httpserver import HTTPServer

from application import Application

define("port", default=8888, help="run on the given port", type=int)

def main():
    parse_command_line()
    #run server
    app = Application()
    http_server = HTTPServer(app, xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()