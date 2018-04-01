from setuptools import setup

setup(
    name='coolsms',
    version='0.2',
    packages=['coolsms'],

    install_requires=[
        'requests>=2.3.0',
    ],
    author='lexifdev',
    author_email='lexifdev@lxf.kr',
    description='''Simple python library for korean SMS service provider CoolSMS(coolsms.co.kr)''',
    license='BSD',
    platforms='any',
)
