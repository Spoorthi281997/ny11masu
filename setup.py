from distutils.core import setup
from setuptools import find_packages
setup(name='ny11masu',
      version='0.1',
      author='DSSS',
      author_email='spoorthi.chinivar@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])