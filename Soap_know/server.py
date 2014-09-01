#coding=utf-8
'''
Created on 2013-11-25

@author: cuckoo5
'''

import tornado.ioloop

from tornado.options import define, options, parse_command_line
from tornado.httpserver import HTTPServer

from soap_know import Application

define("port", default=8888, help="run on the given port", type=int)

def main():
    parse_command_line()
    #run server
    app = Application()
    http_server = HTTPServer(app, xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
#     #注意这种方式下不能启用 autoreload 功能（application 在创建时，debug 参数不能为真）
#     if settings.IPV4_ONLY:
#         import socket
#         sockets = bind_sockets(80, family=socket.AF_INET)
#     else:
#         sockets = bind_sockets(80)
#     if not settings.DEBUG_MODE:
#         import tornado.process
#         tornado.process.fork_processes(0) # 0 表示按 CPU 数目创建相应数目的子进程
#     app = Application()
#     http_server = HTTPServer(app, xheaders=True)
#     http_server.listen(options.port)
#     tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()