from setuptools import setup, find_packages

setup(
    name='multiplexer-manager',
    version='1.1.0',
    author='Steven Linfield',
    author_email='S.Linfield@outlook.com',
    description='Easy analysis of electrochemical data from multiplexer files',
    long_description='README.md',
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'':'src'},
    url='https://github.com/MoonshinetheP/multiplexer-manager',
    keywords='Electrochemistry',
    python_requires=">=3.9",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
    install_requires=['numpy','pandas','matplotlib','scipy'],
)
