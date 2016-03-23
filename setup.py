"""Setup"""
from setuptools import setup

def readme():
    """returns readme string
    """
    with open('README.md') as f:
        return f.read()

setup(
    name='labreporthelper',
    version='0.1',
    description='labreporthelper',
    url='https://github.com/calvinku96/labreporthelper',
    author='Calvin',
    author_email='calvinku96@gmail.com',
    license='MIT',
    packages=['labreporthelper'],
    install_requires=[
        'numpy', 'scipy', 'matplotlib', 'importlib'
    ],
    scripts=['bin/make-lab-report'],
    zip_safe=False)