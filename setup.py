from setuptools import setup, find_packages

setup(
    name='lcloud-task',
    version='0.1',
    entry_points={
        'console_scripts': [
            'lcloud=lcloud:cli.main',  # Call the main function in cli.py
        ],
    },
    install_requires=[
        'click~=8.1.7',
        'boto3~=1.35.24',
        'botocore~=1.35.24',
        'keyring~=25.4.1',
        'setuptools~=75.1.0',
    ],
    author='Ihor Korolenko',
    author_email='korolenkowork275@gmail.com',
    description='A simple CLI package',
    url='https://github.com/EnotShow/LCloud-task/',
)
