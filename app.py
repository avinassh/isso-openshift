#! /usr/bin/python

# This portion of code is fork of gunicorn's example of running
# custom applications.
# Original link - http://gunicorn-docs.readthedocs.org/en/latest/custom.html
# 2009-2015 (c) Benoit Chesneau <benoitc@e-engura.org>
# 2009-2015 (c) Paul J. Davis <paul.joseph.davis@gmail.com>

import os
import sys
import multiprocessing

import gunicorn.app.base
from gunicorn.six import iteritems
from isso import make_app
from isso.core import Config

application = make_app(Config.load('production.cfg'))

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

ip = os.environ['OPENSHIFT_PYTHON_IP']
port = int(os.environ['OPENSHIFT_PYTHON_PORT'])


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % (ip, port),
        'workers': number_of_workers(),
    }
    StandaloneApplication(application, options).run()
