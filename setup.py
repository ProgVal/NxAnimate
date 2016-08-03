#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='nxanimate',
        version='0.1',
        description='Graph algorithms animation tool. Like Gato, but based on NetworkX.',
        author='Valentin Lorentz',
        author_email='progval+nxanimate@progval.net',
        url='https://github.com/ProgVal/nxanimate',
        packages=['nxanimate', 'nxanimate.gui'],
        package_data={
            'nxanimate.gui': [
                'client-resources/animator.js',
                'client-resources/style.css',
                'client-resources/index.html',
                ],
            },
        requires=[
            'networkx',
            'ws4py',
            'cherrypy',
            ],
        classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: JavaScript',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Education',
            'Topic :: Scientific/Engineering :: Visualization',
            ],
        )