from jupyterhub.auth import DummyAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner

import tornado.web

c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = 'test'
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

# Link static files along with templates
c.JupyterHub.extra_handlers = [
    (r'/custom/(.*)', tornado.web.StaticFileHandler, {"path": "custom"}),
]

c.JupyterHub.template_paths = [
    './templates',
]

# QHUB will control these as ways to customize the template
c.JupyterHub.template_vars = {
    'hub_title': 'This is QHub',
    'hub_subtitle': 'your scalable open source data science laboratory.',
    'welcome': 'have fun.',
    'logo': '/hub/custom/images/jupyter_qhub_logo.svg',
}
