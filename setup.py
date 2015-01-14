from setuptools import setup

setup(name='nwanime_dl',
      version='1.1',
      description='downloads anime from nwanime',
      url='https://github.com/thekindlyone/nwanime-dl',
      author='thekindlyone',
      author_email='dodo.dodder@gmail.com',
      license='GNU GPL v2',
      packages=['nwanime_dl'],
      install_requires=[
          'beautifulsoup4',
          'requests'   ],
      scripts=['bin/nwanime-dl'],
      zip_safe=False)