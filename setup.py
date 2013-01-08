try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = 
{
	"description"	: "Weather Widget",
	"author"		: "Stephan Michaud",
	"version"		: "0.1"
}

setup(**config)