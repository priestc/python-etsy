from setuptools import setup, find_packages

setup(
    name='python-etsy',
    version='0.1',
    packages=['etsy',],
    license='BSD',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 0.13.2",
        "requests-oauth >= 0.4.1",
    ],
)
