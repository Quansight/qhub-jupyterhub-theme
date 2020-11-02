c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = 'test'

# since we accept any username for launching we cannot use the default pam spawner
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'

c.JupyterHub.logo_file = 'share/jupyterhub/static/custom/images/jupyter_qhub_logo_small.png'
# we have to manually set the data file path to include custom assets...
c.JupyterHub.data_files_path = './share/jupyterhub'
c.JupyterHub.template_paths = [
    './templates',
    './share/jupyterhub/templates/'
]

# QHUB will control these as ways to customize the template
c.JupyterHub.template_vars = {
    'hub_title': 'This is QHub',
    'hub_subtitle': 'your scalable open source data science laboratory.',
    'welcome': 'have fun.',
}
