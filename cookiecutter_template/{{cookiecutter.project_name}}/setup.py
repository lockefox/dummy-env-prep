"""package control"""
from codecs import open

from setuptools import setup

__package_name__ = '{{cookiecutter.project_name}}'
__version__ = '1.0.0'

with open('README.rst', 'r', 'utf-8') as fh:
    README = fh.read()

with open('requirements.txt', 'r', 'utf-8') as fh:
    REQUIREMENTS = fh.read()

def make_readme():
    """generate README and append `requirements.txt` into it"""
    tabbed_requirements = ['\t' + line for line in REQUIREMENTS.splitlines()]
    return """
{readme}

Includes
========

.. code-block::

    {requirements}

""".format(
        readme=README,
        requirements='\n'.join(tabbed_requirements)
    )

setup(
    name=__package_name__,
    description='{{cookiecutter.project_brief}}',
    long_description=make_readme(),
    version=__version__,
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github_handle}}/' + __package_name__,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='{{cookiecutter.keywords}}',
    package_data={
        '': ['LICENSE', 'README.rst', 'requirements.txt']
    },
    install_requires=REQUIREMENTS.splitlines()
)
