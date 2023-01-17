<p align="center">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/nebari-dev/nebari-design/main/logo-mark/horizontal/Nebari-Logo-Horizontal-Lockup.svg">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nebari-dev/nebari-design/main/logo-mark/horizontal/Nebari-Logo-Horizontal-Lockup-White-text.svg">
  <img alt="Nebari logo mark - text will be black in light color mode and white in dark color mode." src="https://raw.githubusercontent.com/nebari-dev/nebari-design/main/logo-mark/horizontal/Nebari-Logo-Horizontal-Lockup-White-text.svg" width="50%"/>
</picture>
</p>

| Information | Links                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Project     | [![License](https://img.shields.io/badge/License-BSD%203--Clause-gray.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://opensource.org/licenses/BSD-3-Clause) [![Nebari documentation](https://img.shields.io/badge/%F0%9F%93%96%20Read-the%20docs-gray.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://nebari.dev) [![PyPI package version](https://img.shields.io/pypi/v/nebari-jupyterhub-theme.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://pypi.org/project/nebari-jupyterhub-theme/) |
| Community   | [![GH discussions](https://img.shields.io/badge/%F0%9F%92%AC%20-Participate%20in%20discussions-gray.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://github.com/nebari-dev/nebari/discussions) [![Open an issue](https://img.shields.io/badge/%F0%9F%93%9D%20Open-an%20issue-gray.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://github.com/nebari-dev/nebari-jupyterhub-theme/issues/new/choose) [![Nebari documentation - Community guidelines](https://img.shields.io/badge/🤝%20-Community%20guidelines-gray.svg?colorA=2D2A56&colorB=5936D9&style=flat.svg)](https://www.nebari.dev/community/)                                                                                  |

---

# Custom Nebari JupyterHub template

This repository contains a custom JupyterHub template for Nebari.
This template overrides the default JupyterHub templates in <https://github.com/jupyterhub/jupyterhub/tree/main/share/jupyterhub/templates>.

For more details on JupyterHub templates and how they can be used check the official [JupyterHub documentation](https://jupyterhub.readthedocs.io/en/stable/reference/templates.html).

- [Custom Nebari JupyterHub template](#custom-nebari-jupyterhub-template)
  - [Development 👩🏻‍💻](#development-)
    - [Prerequisites](#prerequisites)
    - [Setting your development environment](#setting-your-development-environment)
  - [Using `nebari_jupyterhub_theme` on your JupyterHub instance 📦](#using-nebari_jupyterhub_theme-on-your-jupyterhub-instance-)
  - [Architecture 🏗](#architecture-)
  - [Contributing to `nebari-nebari_jupyterhub_theme`👩‍💻](#contributing-to-nebari-nebari_jupyterhub_theme)
  - [Code of Conduct 📖](#code-of-conduct-)
  - [License 📄](#license-)

## Development 👩🏻‍💻

### Prerequisites

- Python >= 3.8

- We use [Hatch](https://hatch.pypa.io) for development and publishing of the Nebari JupyterHub theme.

  We recommend you install hatch through [pipx](https://hatch.pypa.io/latest/install/#pipx)
  as it modifies the Python environment in which this is installed (for more details, see the [Hatch documentation](https://hatch.pypa.io/latest/install/))

  ```bash
  pipx install hatch
  ```

- [hatch-conda plugin](https://github.com/OldGrumpyViking/hatch-conda). To install:

  ```bash
  pipx install hatch-conda
  ```

### Setting your development environment

1. Make a fork of [the Nebari JupyterHub theme repository][theme-repo] on your personal GitHub account.

1. Clone this repository to your local computer:

   ```bash
   git clone https://github.com/<your-username>/nebari-jupyterhub-theme.git
   ```

1. From the root of the project, create a new development environment with hatch:

   ```bash
   hatch env create
   ```

   This will create a new development environment with all the dependencies needed for development.
   It will also install `nebari_jupyterhub_theme` in development mode.
   You can verify that your development environment is correctly set up by running the following command:

   ```shell
   $ hatch env show
                          Standalone
   ┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
   ┃ Name    ┃ Type    ┃ Dependencies            ┃ Scripts ┃
   ┡━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
   │ default │ virtual │                         │         │
   ├─────────┼─────────┼─────────────────────────┼─────────┤
   │ dev     │ virtual │ configurable-http-proxy │ render  │
   │         │         │ jupyterhub              │         │
   │         │         │ jupyterlab              │         │
   │         │         │ nodejs                  │         │
   └─────────┴─────────┴─────────────────────────┴─────────┘
   ```

1. Initialize a new shell within the development environment:

   ```bash
   hatch --env dev shell
   ```

   To leave the environment you can type `exit` on your terminal.

1. Initialize a JupyterHub instance for development:

   ```bash
   hatch run dev:render
   ```

   This command will start JupyterHub with the `--config` option pointing to [`test_jupyterhub_config.py`](test_jupyterhub_config.py).
   You should be able to head to <http://127.0.0.1:8081> on your web browser and see the JupyterHub instance running.

   ![Login page of a local JupyterHub instance with the Nebari JupyterHub theme - the main text reads "welcome to Nebari your open source data science platform". The subheading reads "Running in dev mode". In the middle of the page there is the JupyterHub authentication form with a "username" and "password" fields.](images/Nebari-JupyterHub-login.png)

   > **Note**
   > From here you can log in with any username and the password set in the `c.DummyAuthenticator.password` configuration option in [`test_jupyterhub_config.py`](test_jupyterhub_config.py). Also note not all the extensions and integrations are available in this `dev` mode.

1. You can now modify the templates and the `style.css` file and see the changes reflected in the JupyterHub instance without having to restart the server.

> **Note**
> The values specified in `c.JupyterHub.template_vars` will overwrite the default values set in `nebari_jupyterhub_theme/templates`

The release process for this package is documented in [`RELEASE.md`](RELEASE.md).

## Using `nebari_jupyterhub_theme` on your JupyterHub instance 📦

1. Install `nebari_jupyterhub_theme`:

   ```bash
   pip install nebari_jupyterhub_theme
   ```

   > **Note**
   > If you already have a JupyterHub configuration file you can jump to the next step. Otherwise, follow the instructions in the [JupyterHub documentation](https://jupyterhub.readthedocs.io/en/stable/getting-started/config-basics.html) to generate a configuration file first.

2. Add the following to you JupyterHub configuration file to pick up the new `jinja2` templates directory and static files:

   ```python
   from nebari_jupyterhub_theme import theme_extra_handlers, theme_template_paths

   c.JupyterHub.extra_handlers = theme_extra_handlers

   c.JupyterHub.template_paths = theme_template_paths
   ```

3. **Optional** - if you need to further customize the UI you can modify the `template_vars` within your JupyterHub config file by adding the following lines to it:

   ```python
   # minimal configuration example overwriting the default values in the nebari_jupyterhub_theme
   c.JupyterHub.template_vars = {
    "hub_title": "Welcome to Nebari",
    "logo": "/hub/custom/images/Nebari-logo-square.svg",
    "primary_color": "#cb39ed",
    "secondary_color": "#2bd1c5",
   ```

The available configuration variables are:

- `hub_title`: The title of the JupyterHub instance. This will be displayed in the header of the login page. (H1 heading, `default: Welcome to Nebari`)
- `hub_subtitle`: Subtitle shown under the main instance Title. (H2 heading, `default: ""`)
- `welcome`: Welcome message on the login page (`default:  Welcome to Nebari. For more information about Nebari, visit <a href="https://nebari.dev/">https://nebari.dev</a>`)
- `logo`: Logo displayed on the navbar (`default: Nebari logomark`)
- `primary_color`: Primary color (`default:` `#9e17b7`)
- `secondary_color`: Secondary color (`default:` `#2bd1c5`)
- `accent_color`: Accent color (`default:` `#eda61d`)
- `text_color`: Text color (`default:` `#1c1d26`)
- `h1_color`: H1 color, main Title in login page (`default:` `#0f1015`)
- `h2_color`: H2 color, subtitle in login page (`default:` `#0f1015`)
- `navbar_text_color`: Navigation bar links and text color (`default:` `#1c1d26`)
- `navbar_hover_color`: Hover color for navigation bar links (`default:` `#00a3b0`)
- `display_version`: Display the JupyterHub version in the footer (`default: False`)

> **Note**
> The default colors, typefaces and logos are chosen based on the Nebari branding. You can find more about this on the [Nebari design repository](https://github.com/nebari-dev/nebari-design).

:computer: You can see an example of these variables and the configuration in [`test_jupyterhub_config.py`](test_jupyterhub_config.py).

Nebari internal options:
- `cdsdashboards_enabled`: This requires [cdsdashboards](https://github.com/ideonate/cdsdashboards) to be present in the JupyterHub environment (`default: False`)
- `cdsdashboards_restricted`: This requires [cdsdashboards](https://github.com/ideonate/cdsdashboards) to be present in the JupyterHub environment (`default: False`)
- `nebari_theme_extra_js_urls`

## Architecture 🏗

This repository is structured as follows:

- [.github](.github): GitHub Actions configuration files and repository templates
- [images](images/): Images used in this README
- [nebari_jupyterhub_theme](nebari_jupyterhub_theme/): Python package containing the `jinja2` templates and static files
- [pyproject.toml](pyproject.toml): Python project configuration file
- [test_jupyterhub_config.py](test_jupyterhub_config.py): Example JupyterHub configuration file - used by `hatch run dev:render` to start a local JupyterHub instance for local development.
- [RELEASE.md](RELEASE.md): Release process documentation
- [.pre-commit-config.yaml](.pre-commit-config.yaml): Configuration file for the [pre-commit](https://pre-commit.com/) tool (note we use pre-commit CI to automatically run pre-commit on all PRs and update the hooks)

## Contributing to `nebari-nebari_jupyterhub_theme`👩‍💻

Thinking about contributing? Check out our [Contribution Guidelines](CONTRIBUTING.md) to get started.

## Code of Conduct 📖

To guarantee a welcoming and friendly community, we require all community members to follow our [Code of Conduct](https://github.com/Quansight/.github/blob/master/CODE_OF_CONDUCT.md).

## License 📄

`nebari-nebari_jupyterhub_theme` is licensed under the [BSD-3 OSI licenses](https://github.com/nebari-dev/nebari-docs/blob/main/LICENSE).

<!-- links -->
[theme-repo]: https://github.com/nebari-dev/nebari-jupyterhub-theme
