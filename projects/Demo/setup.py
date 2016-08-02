try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'demo',
'author': 'chen wen hua',
'telephone': '12331232',
'url': 'URL to get it at.', 
'download_url': 'Where to download it.', 
'author_email': 'My email.',
'version': '0.1',
'install_requires': ['nose'], 'packages': ['doll','bin'], 
'name': 'Demo',
'scripts': ['./bin/temp'],

}


