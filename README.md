# Custom JupyterHub Template for QHub

This repo contains html jinja2 templates for customising the
appearance of JupyterHub. Each HTML file here will override the files
in https://github.com/jupyterhub/jupyterhub/tree/master/share/jupyter/hub/templates.

## Usage

To use this repo ensure it is checked out and available somewhere that
JupyterHub can find it. Add to the jupyterhub configuration to pickups
the new jinja2 templates directory and static files.

```python
import tornado.web

c.JupyterHub.extra_handlers = [
    (r'/custom/(.*)', tornado.web.StaticFileHandler, {"path": "custom"}),
]

c.JupyterHub.template_paths = [
    './templates',
]
```

Finally customize the templates via the `template_vars`. Current
options are:
 - `hub_title`
 - `hub_subtitle`
 - `welcome`
 - `logo`
 
Inspiration is in the test jupyterhub configuration
`test_jupyterhub_config.py`.

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
