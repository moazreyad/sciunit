#!/usr/bin/env python
import os
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py


def localopen(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


class BuildCommand(build_py):
    def run(self):
        subprocess.check_call(['cmake', '-DCMAKE_BUILD_TYPE=Release'])
        subprocess.check_call(['make'])
        build_py.run(self)


setup(
    name='sciunit2',
    version='0.1',
    description='Sciunit command line',
    author='Zhihao Yuan',
    author_email='zhihao.yuan@depaul.edu',
    packages=["sciunit2"],
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    keywords=['sciunit'],
    url='https://bitbucket.org/geotrust/sciunit2/src',
    long_description=localopen('README.rst').read(),
    install_requires=localopen('requirements.txt').readlines(),
    tests_require=localopen('test-requirements.txt').readlines(),
    cmdclass={'build_py': BuildCommand},
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Science/Research',
    ]
)
