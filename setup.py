from setuptools import setup, find_packages

setup(
    name='multiplexer-manager',
    version='1.0.4',
    readme="README.md",
    license = "GPL3",
    author='Steven Linfield',
    author_email='S.Linfield@outlook.com',
    description='Easy analysis of multiplexer files',
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
    install_requires=['numpy','pandas'],
)
