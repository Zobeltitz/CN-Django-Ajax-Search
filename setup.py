import os
from setuptools import setup

#README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ajax-search',
    version=__import__('ajax_search').__version__,
    packages=['ajax_search'],
    include_package_data=True,
    license='BSD',
    description='A customizable AJAX-powered search for Django.',
    long_description=open('README.txt').read(),
    url='http://prasenjitsingh.com/opensource/django-ajax-search/',
    author='Prasenjit Singh',
    author_email='prasenjit0625@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
		'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
	zip_safe=False,
)