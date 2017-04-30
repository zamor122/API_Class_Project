#setup.py

from distutils.core import setup
import py2exe

setup(
    name='googlePlacesClient',
    version='1.0',
    url='https://github.com/zamor122/AroundME.git',
    author='Shayne Zamora',
    packages=['googleplaces'],
    console=['main.py']
)