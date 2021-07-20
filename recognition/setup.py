import os

import pkg_resources
from setuptools import setup, find_packages

with open('arcface_torch/README.md') as f:
    long_description = f.read()

setup(
    name='arcface_torch',
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "arcface_torch/requirement.txt"))
        )
    ],

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/deepinsight/insightface',

)
