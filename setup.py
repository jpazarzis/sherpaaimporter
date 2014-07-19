import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sherpaaimporter",
    version = "0.0.1",
    author = "John Pazarzis",
    author_email = "jpazarzis@gmail.com",
    description = ("coding test"),
    license = "BSD",
    keywords = "sherpa data import",
    url = "http://www,codingismycraft.com",
    packages=['sherpaautils',],
    long_description=read('README'),
)
