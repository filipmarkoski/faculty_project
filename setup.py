"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='faculty',
    version='0.1.0',
    license='proprietary',
    description='Student Project Faculty',

    author='Filip Markoski',
    author_email='filip.markoski45@gmail.com',

    # packages=find_packages(exclude=('tests', 'docs', 'venv'))
    packages=find_packages(where='src'),
    package_dir={'': 'src'}

)
