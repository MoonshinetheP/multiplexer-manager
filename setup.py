from setuptools import setup, find_packages

setup(
    name='multiplexermanager',
    version='1.0.1',
    author='Steven Linfield',
    author_email='steven.linfield@softpotato.xyz',
    packages=find_packages('src'),
    package_dir={'':'src'},
    url='https://github.com/MoonshinetheP/multiplexer-manager',
    keywords='Electrochemistry',
    install_requires=[
    'numpy',
	'pandas',
    ],
)
