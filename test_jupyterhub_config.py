from jupyterhub.auth import DummyAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner

from qhub_jupyterhub_theme import theme_extra_handlers, theme_template_paths

c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = 'test'
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

# Link static files along with templates
c.JupyterHub.extra_handlers = theme_extra_handlers

c.JupyterHub.template_paths = theme_template_paths

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
    'navbar_text_color': '#E8E8E8',
    'narbar_hover_color': '#00a3b0',
    # 'qhub_theme_extra_js_urls': ['https://google.com/qhub.js']
}
