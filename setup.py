# Import third-party modules
from setuptools import find_packages
from setuptools import setup

# Import local modules
import photoshop_python_api

SHORT = ('photoshop_python_api is a python api that connects photoshop with '
         'COM.')
LONG = ('photoshop_python_api is a python api that connects photoshop with '
        'COM. For more info check out the README at '
        '\'github.com/loonghao/photoshop_python_api\'.')

setup(
    name='photoshop_python_api',
    package_dir={'': '.'},
    packages=find_packages('.'),
    url='https://github.com/loonghao/photoshop_python_api',
    author=photoshop_python_api.__author__,
    version=photoshop_python_api.__version__,
    author_email='hoolongvfx@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description=SHORT,
    long_description=LONG,
    install_requires=['comtypes'],
    package_data={'': ['LICENSE']},
)
