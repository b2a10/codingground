try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'BA',
    'url': 'URL to get it at.',
    'download_url':'Where to download it.',
    'author_email':'14b**************@***********.com',
    'verion': '0.1',
    'install_requires':['nose'], # don't currently have this
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)