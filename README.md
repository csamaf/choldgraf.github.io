# Personal website and blog

This site is inspired by and copied from https://github.com/choldgraf/choldgraf.github.io.

## Building the site locally

The current [requirements.txt](requirements.txt) are known to work with Python 3.11.

### Using make

Following the [deploy.yml](.github/workflows/deploy.yml) workflow by executing

```bash
python3.11 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
make dirhtml
```

should generate the site in `_build`, which can be opened with

```bash
xdg-open _build/dirhtml/index.html &
```

### Using nox

We also ship a [noxfile.py](noxfile.py) to generate the site using [nox](https://github.com/wntrblm/nox) with

```bash
pipx nox -s docs  # omit pipx if you have nox installed
```

and to run a live web-server with

```bash
pipx nox -s docs -- live
```

which watches for local changes.

