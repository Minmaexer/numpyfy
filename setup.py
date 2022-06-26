from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='numpyfy',
    version='0.0.1',
    description='A simple tool for converting different filetypes to numpy arrays',
    py_modules=['numpyfy'],
    package_dir={'': 'src'},
    url='https://github.com/Minmaexer/numpyfy',
    author='Patricio Reller',
    author_email='minmaexer@proton.me',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Operating System :: OS Independent',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy'],
    extras_require={
        'dev': ['pytest>=3.7',
                'Mock>=3.0.0',
                'pytest-cov>=2.6.0'],
    },
)
