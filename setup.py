from setuptools import setup

setup(name='Isso OpenShift',
      version='0.1',
      description='This kit helps you install Isso on OpenShift with single click',
      author='Avinash Sajjanshetty',
      author_email='hi@avi.im',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['isso', 'gunicorn', 'passlib'],
     )