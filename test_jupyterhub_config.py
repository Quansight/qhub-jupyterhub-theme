from jupyterhub.auth import DummyAuthenticator
from jupyterhub.spawner import SimpleLocalProcessSpawner

from nebari_jupyterhub_theme import theme_extra_handlers, theme_template_paths

c.JupyterHub.authenticator_class = DummyAuthenticator
c.DummyAuthenticator.password = "test"
c.JupyterHub.spawner_class = SimpleLocalProcessSpawner

# Link static files along with templates
c.JupyterHub.extra_handlers = theme_extra_handlers

c.JupyterHub.template_paths = theme_template_paths

# nebari will control these as ways to customize the template
c.JupyterHub.template_vars = {
    "hub_title": "Welcome to Nebari",
    "hub_subtitle": "your open source data science platform",
    "welcome": "Running in dev mode",
    "logo": "/hub/custom/images/Nebari-Logo-Horizontal-Lockup-White-text.svg",
    "primary_color": "#cb39ed",
    "secondary_color": "#2bd1c5",
    "accent_color": "#eda61d",
    "text_color": "#1c1d26",
    "h1_color": "#0f1015",
    "h2_color": "#0f1015",
    "navbar_text_color": "#E8E8E8",
    "narbar_hover_color": "#00a3b0",
    "navbar_color": "#1c1d26",
    # "display_version": "True",
    # "nebari_theme_extra_js_urls": ["https://google.com/qhub.js"],
}
