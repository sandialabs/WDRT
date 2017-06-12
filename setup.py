from setuptools import setup

#Preliminary setup.py file for WDRT
setup(
    name = "WDRT",
    version = "1.0.0",
    url = "https://github.com/WEC-Sim/WDRT",
    install_requires=['numpy', 'scipy', 'requests', 'bs4', 'sklearn','matplotlib'],
    packages=['WDRT', 'examples'],
)