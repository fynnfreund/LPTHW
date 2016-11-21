try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'EX47 from LPTHW',
    'author': 'Fynn Freund',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'fynn.freund@stud.leuphana.de'
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Name'],
    'scripts': [],
    'name': 'EX47'
}

setup(**config)
