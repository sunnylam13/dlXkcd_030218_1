try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A program that can be used to download XKCD webcomics.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/dlXkcd_030218_1',
	'download_url': 'https://github.com/sunnylam13/dlXkcd_030218_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['requests, os, bs4'],
	'scripts': [],
	'name': 'Download XKCD Comics'
}

setup(**config)