**Please submit issues to https://github.com/quansight/qhub/issues**

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
from qhub_jupyterhub_theme import theme_extra_handlers, theme_template_paths

c.JupyterHub.extra_handlers = theme_extra_handlers

c.JupyterHub.template_paths = theme_template_paths
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

 Internal options:
 - `cdsdashboards_enabled`
 - `cdsdashboards_restricted`
 - `qhub_theme_extra_js_urls`

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

To run in VSCode, here is a launch.json config:
```
{
    "name": "JupyterHub test",
    "type": "python",
    "request": "launch",
    "module": "jupyterhub",
    "args": ["-f", "./test_jupyterhub_config.py"],
    "cwd": "${workspaceFolder}"
}
```
You would need to make sure the Python virtualenv you've set up for this is active in the project.

## Changelog

Version 0.3.3
- Simplify the JupyterHub config (backwards-compatible)
