import os
import tornado.web

HERE = os.path.dirname(__file__)

TEMPLATE_PATH = os.path.join(HERE, 'templates')
STATIC_PATH = os.path.join(HERE, 'custom')

theme_extra_handlers = [
    (r'/custom/(.*)', tornado.web.StaticFileHandler, {"path": STATIC_PATH}),
]

theme_template_paths = [ TEMPLATE_PATH ]
