from setuptools import setup
import os
try:
    import pypandoc
    description=pypandoc.convert('readme.md','rst')
except:
    description=''
setup(name='nwanime_dl',
      version='1.9.1',
      description='downloads anime from nwanime',
      long_description=description,
      url='https://github.com/thekindlyone/nwanime-dl',
      author='thekindlyone',
      author_email='dodo.dodder@gmail.com',
      license='GNU GPL v2',
      packages=['nwanime_dl'],
      install_requires=[
          'beautifulsoup4',
          'lxml',
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
