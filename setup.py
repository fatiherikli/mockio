from distutils.core import setup

setup(name='Mockio',
      version='0.1',
      description='Mock open method with StringIO',
      author='Fatih Erikli',
      author_email='fatiherikli@gmail.com',
      url='https://github.com/fatiherikli/mockio',
      packages=['mockio'],
      install_requires = [
          'mock==1.0.1',
      ]
)