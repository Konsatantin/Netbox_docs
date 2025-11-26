from setuptools import find_packages, setup

setup(
    name='netbox-documents',
    version='0.2',
    description='A plugin to store documents in NetBox',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
