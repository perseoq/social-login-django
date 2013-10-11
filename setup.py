import os
from setuptools import setup
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
setup(name='django-loginradius',
    version='0.1',
    packages=['django_loginradius'],
    requires=['Django (>=1.4)',],
    license='The MIT License file',
    description='Django Authentication support for LoginRadius. Provides social authentication for 25+ social providers',
    long_description=README,
    url='https://www.loginradius.com/',
    author='LoginRadius Team',
    author_email='deepak@loginradius.com'
)
