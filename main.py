#!/usr/bin/env python

import cherrypy
import os

class CherryPySampleApp(object):
    def index(self):
        return open(u'public/index.html')
    index.exposed = True

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.join(os.path.abspath(os.getcwd()), "public"),
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '.'
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(CherryPySampleApp(), config=conf)
