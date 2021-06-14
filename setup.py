
import pathlib
from setuptools import setup


__version__ = '0.0.1'
__author__ = 'Dhruv'


HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()


setup(
    name = 'crypto',
    version = __version__,
    description = 'A Crpyto price checker',
    long_description = README,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/datdhruvjain/Crypto-Price',
    author = __author__,
    license = 'MIT',
    
    classifiers = [
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages = ['CryptoPrice'],
    include_package_data = True,
    install_requires = [
    'art==5.2',
    'certifi==2021.5.30',
    'chardet==4.0.0',
    'colorama==0.4.4',
    'idna==2.10',
    'requests==2.25.1',
    'urllib3==1.26.5'
    ],

    entry_points = {'console_scripts': ['crypto=CryptoPrice.__main__:main']},
)