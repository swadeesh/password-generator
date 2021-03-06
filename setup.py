import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pypassword-generator',
    version='0.1.0',
    author='Swadeesh',
    author_email='swadeesh@gmail.com',
    description='A PyPI Package helps to generate random passwords.',
    keywords='random password, pypassword',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/swadeesh/password-generator',
    project_urls={
        'Documentation': 'https://github.com/swadeesh/password-generator',
        'Bug Reports': 'https://github.com/swadeesh/password-generator/issues',
        'Source Code': 'https://github.com/swadeesh/password-generator',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=['multipledispatch'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=pypassword:main',
    # You can execute `run` in bash to run `main()` in src/pypassword/__init__.py
    #     ],
    # },
)
