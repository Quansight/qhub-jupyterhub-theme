# Copyright (c) Nebari Development Team.
# Distributed under the terms of the Modified BSD License.

from pathlib import Path

import tornado.web

HERE = Path(__file__).parent.resolve()

TEMPLATE_PATH = HERE.joinpath("templates")
STATIC_PATH = HERE.joinpath("custom")

theme_extra_handlers = [
    (r"/custom/(.*)", tornado.web.StaticFileHandler, {"path": STATIC_PATH}),
]

theme_template_paths = [TEMPLATE_PATH]
