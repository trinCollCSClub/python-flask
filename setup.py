try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My first Website',
    'author': 'Will Estony',
    'url': 'URL to get at it.',
    'download_url': 'Where to download it.',
    'author_email': 'williamestony@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'flask'],
    'packages': ['gothonweb'],
    'scripts': ['gothonweb/app.py'],
    'name': 'gothonweb',
}

setup(**config)