import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="bigdatacloudapi-client",
    version="1.0.1",
    description="A Python client for BigDataCloud API connectivity (https://www.bigdatacloud.net)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bigdatacloudapi/python-api-client",
    author="BigDataCloud",
    author_email="support@bigdatacloud.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["bigdatacloudapi"],
    install_requires=["requests"]
)