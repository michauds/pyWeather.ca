from setuptools import setup

def readme():
    with open('README.md') as file:
        return file.read()

setup(name='pyweather',
      version='0.1',
      description='Fetches xml data from Environment Canada and polls your current city's weather',
      url='http://github.com/michauds/pyweather',
      author='Stephan Michaud',
      author_email='michauds90@gmail.com',
      packages=['pyweather'],
      install_requires=[
          'json',
          'xml',
          'urllib2',
	  'csv',
          'ConfigParser',
      ],
      zip_safe=False)
