try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Sense based artificial neural network for rating suggestion',
    'author': 'Fabio Colella',
    'url': 'https://github.com/fcole90/semblance',
    'download_url': 'https://github.com/fcole90/semblance',
    'author_email': 'fcole90@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],
    'name': 'semblance'
}

setup(**config)
