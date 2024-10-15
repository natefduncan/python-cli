from setuptools import setup, find_packages

def get_reqs():
    with open("./requirements.txt", "r") as f:
        return f.readlines()

setup(
    name='package_name',
    version='0.1.0',
    packages=find_packages(), 
    include_package_data=True, 
    install_requires=get_reqs(),
    entry_points={
        'console_scripts': [
            'package_name = package_name.main:cli',
        ],
    },
)
