import os.path

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


__authors__     = 'Scott Torborg, Michael Stella'
__credits__     = ['Scott Torborg', 'Michael Stella']
__license__     = 'GPL'
__maintainer__  = 'Scott Torborg'
__status__      = 'Development'
__version__     = '0.3.1'

           
setup(name='packagetrack',
      version=__version__,
      author="Scott Torborg",
      author_email="storborg@mit.edu",
      license="GPL",
      keywords="track packages ups fedex usps shipping",
      url="http://github.com/storborg/packagetrack",
      description='Track packages.',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      install_requires=[
          'fedex'
      ],
      long_description=read('README.rst'),
      test_suite='nose.collector',
      zip_safe=False,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Programming Language :: Python"])
