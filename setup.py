from distutils.core import setup

setup(
    name='ismdeep-utils',  # How you named your package folder (MyLib)
    packages=['ismdeep_utils'],  # Chose the same as "name"
    version='0.1.4',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='ismdeep-utils',  # Give a short description about your library
    author='ismdeep',  # Type in your name
    author_email='ismdeep@protonmail.com',  # Type in your E-Mail
    url='https://github.com/ismdeep/ismdeep-utils-py',  # Provide either the link to your github or to your website
    keywords=['utils', 'args'],  # Keywords that define your package best
    install_requires=[
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: MIT License",
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
