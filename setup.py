from setuptools import setup
setup(
    name = 'awsprofile',
    version = '1.0.0',
    packages = ['awsprofile'],
    entry_points = {
        'console_scripts': [
            'awsprofile = awsprofile.__main__:main'
        ]
    })
