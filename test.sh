#!/usr/bin/env bash

mkdir -p share
cp -r $(python -c "import jupyterhub.app; print(jupyterhub.app.DATA_FILES_PATH)") share
chmod -R 755 share
# we have to copy assets since jupyterhub does not have an easy way to add static paths...
cp -r extra-assets/css extra-assets/images share/jupyterhub/static/custom

jupyterhub --config test_jupyterhub_config.py
