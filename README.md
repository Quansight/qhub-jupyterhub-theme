# Custom JupyterHub Template for QHub

This repo contains html jinja2 templates for customising the
appearance of JupyterHub. Each HTML file here will override the files
in https://github.com/jupyterhub/jupyterhub/tree/master/share/jupyter/hub/templates.

## Usage

Install `qhub_jupyterhub_theme` in your environment

```shell
pip install qhub_jupyterhub_theme
```

Add the following to the jupyterhub configuration to pickup the new
jinja2 templates directory and static files.

```python
import tornado.web
import qhub_jupyterhub_theme

c.JupyterHub.extra_handlers = [
    (r'/custom/(.*)', tornado.web.StaticFileHandler, {"path": qhub_jupyterhub_theme.STATIC_PATH}),
]

c.JupyterHub.template_paths = [
    qhub_jupyterhub_theme.TEMPLATE_PATH
]
```

Finally customize the templates via the `template_vars`. Current
options are:
 - `hub_title`
 - `hub_subtitle`
 - `welcome`
 - `logo`
 - `primary_color`
 - `secondary_color`
 - `accent_color'`
 - `text_color`
 - `h1_color`
 - `h2_color`
 - `cdsdashboards_enabled`

Inspiration is in the test jupyterhub configuration
`test_jupyterhub_config.py`.

```python
c.JupyterHub.template_vars = {
    'hub_title': 'This is QHub',
    'hub_subtitle': 'your scalable open source data science laboratory.',
    'welcome': 'have fun.',
}
```

## Testing

Install the development environment

```shell
conda env install -f environment.yaml
```

You do not need to restart jupyterhub to see changes in `custom` and
`templates`. Run jupyterhub via the test script

```shell
jupyterhub --config test_jupyterhub_config.py
```
