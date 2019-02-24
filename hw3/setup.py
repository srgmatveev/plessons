from setuptools import setup
setup(
    name="wsgi",
    version="0.1",
    license="BSD",
    packages=['wsgi', 'test'],
    install_requires=['uwsgi'],
)
