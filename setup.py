import os
import shutil

from setuptools import setup, find_packages, Command

try:
    from certvalidator import version
    __version__ = version.__version__
except ImportError:
    # __init__.py is loaded and fails with oscrypto, there is probably a better
    # way to deal with this than exec
    exec(open('certvalidator/version.py').read())

class CleanCommand(Command):
    user_options = [
        ('all', 'a', '(Compatibility with original clean command)')
    ]

    def initialize_options(self):
        self.all = False

    def finalize_options(self):
        pass

    def run(self):
        folder = os.path.dirname(os.path.abspath(__file__))
        for sub_folder in ['build', 'dist', 'certvalidator.egg-info']:
            full_path = os.path.join(folder, sub_folder)
            if os.path.exists(full_path):
                shutil.rmtree(full_path)


setup(
    name='certvalidator',
    version=__version__,

    description='Validates X.509 certificates and paths',
    long_description='Docs for this project are maintained at https://github.com/wbond/certvalidator#readme.',

    url='https://github.com/wbond/certvalidator',

    author='wbond',
    author_email='will@wbond.net',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Topic :: Security :: Cryptography',
    ],

    keywords='crypto pki x509 certificate crl ocsp',

    install_requires=[
        'asn1crypto>=0.22.0',
        'oscrypto>=0.18.0'
    ],
    packages=find_packages(exclude=['tests*', 'dev*']),

    test_suite='tests.make_suite',

    cmdclass={
        'clean': CleanCommand,
    }
)
