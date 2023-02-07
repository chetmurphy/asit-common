from setuptools import setup

setup(
    name='asit-common',
    version='0.1.0',    
    description='Configuration and common shared code for the ASIT scripting environment',
    url=' https://github.com/chetmurphy/asit-common.git',
    author='Chet Murphy',
    author_email='chetmurphy@hotmail.com',
    license='MIT',
    packages=['asit-common'],
    install_requires=['mpi4py>=2.0'              
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: Windows',        
        'Programming Language :: Python :: 3.7',
    ],
)