from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
share_qhub_jupyterhub_theme = os.path.join(here, 'share', 'qhub_jupyterhub_theme')


# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="qhub_jupyterhub_theme",
    version='0.3.6',
    description="QHub jupyterhub theme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quansight/qhub-jupyterhub-theme",
    author="Quansight",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="jupyterhub theme",
    packages=['qhub_jupyterhub_theme'],
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4",
    install_requires=[
        "jupyterhub"
    ],
    package_data={
        'qhub_jupyterhub_theme': [
            'templates/*',
            'custom/css/*',
            'custom/images/*'
        ]
    },
    include_package_data=True,
    project_urls={
        "Bug Reports": "https://github.com/Quansight/qhub-jupyterhub-theme",
        "Source": "https://github.com/Quansight/qhub-jupyterhub-theme",
    },
)
