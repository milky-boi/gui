from setuptools import setup
import os
home=os.path.expanduser('~')

with open('description.txt') as f:
    long_description = f.read()

setup(
    name = 'flyGUI',
    version = '0.2',
    description = 'GUI for data selection and visualization',
    long_description = long_description,
    url=' ',
    license='GPL v3',
    author = 'Milan Petrovic',
    author_email = '@gmail.com',
    install_requires=[
	'matplotlib>=2.0',
	'pandas>=0.18',
	'tkinter>=2.4'
	],
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Topic :: Software Development :: User Interfaces',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Development Status :: Alpha',
            'Intended Audience :: Science/Research'],
    keywords = ['tkinter', 'ttk', 'table', 'pandas', 'data analysis', 'data visualization'],
)