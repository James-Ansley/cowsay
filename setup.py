import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-cowsay',
    version='1.0.1',
    author='James Finnie-Ansley',
    description='A Cowsay clone in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/James-Ansley/cowsay',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(
        where='src',
    ),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>=3.8',
)
