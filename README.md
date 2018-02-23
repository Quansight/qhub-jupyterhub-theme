# Custom JupyterHub Templates for Jade/Pangeo

This repo contains html jinja2 templates for customising the appearance of JupyterHub. Each HTML file here will override the files in `https://github.com/jupyterhub/jupyterhub/tree/master/share/jupyter/hub/templates`.

## Usage

To use this repo ensure it is checked out and available somewhere that JupyterHub can find it. In thie example we will assume we have cloned it somewhere and created the following symlinks

`/path/to/repo/templates` -> `/usr/local/share/jupyter/hub/custom_templates`
`/path/to/repo/assets` -> `/usr/local/share/jupyter/hub/static/custom`

Add the following to your JupyterHub config

```python
c.JupyterHub.logo_file = '/usr/local/share/jupyter/hub/static/custom/images/logo.png'
c.JupyterHub.template_paths = ['/usr/local/share/jupyter/hub/custom_templates/',
                                '/usr/local/share/jupyter/hub/templates/']
```
