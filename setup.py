
from setuptools import setup, find_packages
import base

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='base',
        version=base.__version__,
        description='Sample Python project structure',
        long_description=readme,
        author='Jaehoon Chung',
        author_email='jaehoon92@gmail.com',
        url='https://github.com/jaehoon92/base',
        license=license,
        packages=find_packages(exclude=('tests', 'docs'))
)
