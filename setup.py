from setuptools import setup
import os
def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
setup(name='nwanime_dl',
      version='1.8.4',
      description='downloads anime from nwanime',
      long_description=(read('readme.rst')),
      url='https://github.com/thekindlyone/nwanime-dl',
      author='thekindlyone',
      author_email='dodo.dodder@gmail.com',
      license='GNU GPL v2',
      packages=['nwanime_dl'],
      install_requires=[
          'beautifulsoup4',
          'requests'   ],
      scripts=['bin/nwanime-dl'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 2.7"          
      ],
      zip_safe=False)