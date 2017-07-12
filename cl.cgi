#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from cl import app

CGIHandler().run(app)