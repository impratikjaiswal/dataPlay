# -*- coding: UTF−8 -*-

import os

from setuptools import setup, find_packages

from data_play.main.helper.constants_config import ConfigConst

# all packages dependencies
packages = find_packages()
if not packages:
    print(f'Selecting Hardcoded Packages')
    packages = [
        "data_play.main",
        "data_play.test",
    ]
print(f'Packages are {packages}')
# potential dependencies
install_reqs = [
    'incremental',
    'click',
    'twisted',
]

setup_reqs = [
    'incremental',
]

# get long description from the README.md
with open(os.path.join(os.path.dirname(__file__), "README.md"), "r", encoding="utf-8") as fd:
    long_description = fd.read()

setup(
    use_incremental=True,
    setup_requires=setup_reqs,
    name=ConfigConst.TOOL_NAME,
    author="Pratik Jaiswal",
    author_email="impratikjaiswal@gmail.com",
    description="Generic TLV Parser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/impratikjaiswal/dataPlay",
    project_urls={
        "Bug Tracker": "https://github.com/impratikjaiswal/dataPlay/issues",
    },
    keywords="Data Generator",
    license="MIT",
    python_requires=">=3.9",
    packages=packages,
    install_requires=install_reqs
    # test_suite="test.sample_package",
)