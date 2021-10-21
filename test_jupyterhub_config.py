from jupyterhub.auth import DummyAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner

import tornado.web

c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = 'test'
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

# Link static files along with templates
c.JupyterHub.extra_handlers = [
    (r'/custom/(.*)', tornado.web.StaticFileHandler, {"path": "./qhub_jupyterhub_theme/custom"}),
]

c.JupyterHub.template_paths = [
    './qhub_jupyterhub_theme/templates',
]

# QHUB will control these as ways to customize the template
c.JupyterHub.template_vars = {
    'hub_title': 'This is QHub',
    'hub_subtitle': 'your scalable open source data science laboratory.',
    'welcome': 'have fun.',
    'logo': '/hub/custom/images/jupyter_qhub_logo.svg',
    'primary_color': '#4f4173',
    'secondary_color': '#957da6',
    'accent_color': '#32C574',
    'text_color': "#111111",
    'h1_color': "#652e8e",
    'h2_color': "#652e8e",
#    'qhub_theme_extra_js_urls': [{
#        'src': 'https://static.zdassets.com/ekr/snippet.js?key=yourkey',
#        'id':  'snippet'
#    }, "https://google.com/qhub.js"]
}
