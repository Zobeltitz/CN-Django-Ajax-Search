import os
from setuptools import setup

#README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

#允许从任何路径运行
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ajax-search-cn',
    version=__import__('ajax_search').__version__,
    packages=['ajax_search'],
    include_package_data=True,
    license='BSD',
    description='基于Django与Ajax的搜索引擎',
    long_description=open('README.txt').read(),
    url='https://github.com/Zobeltitz/django-ajax-search',
    author='Zobeltitz 中国',
    author_email='admin@ixiling.com',
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
