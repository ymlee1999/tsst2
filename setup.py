from setuptools import setup, find_packages
setup(
        name="mypkg", # pip install 할 때 사용되는이름
        version="0.1.0",
        packages=find_packages(),
)