from setuptools import setup, find_packages

setup(
    name="my_test_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    description="A sample package for testing the iflow-engine deployment endpoint",
)
