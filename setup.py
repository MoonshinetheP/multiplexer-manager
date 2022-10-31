from setuptools import setup, find_packages

setup(
    name='multiplexermanager',
    version='1.0.0',
    author='Steven Linfield',
    author_email='S.Linfield@outlook.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    url='https://github.com/MoonshinetheP/multiplexer-manager',
    keywords='Electrochemistry',
    install_requires=[
    'numpy',
	'pandas',
    ],
)
