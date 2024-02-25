from setuptools import setup, find_packages

setup (
    name='AlxPackages',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    License='MIT',
    long_description=open('Readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/aihatim/Alx',
    author='aihatim',
    author_email='aith.hatim.ai@gmail.com',

)