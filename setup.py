from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='asreview-reusable-fe',
    version='1.0',
    description='asreview-reusable-fe',
    url='https://github.com/jteijema/asreview-reusable-fe',
    author='Jelle Teijema',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.6',
    install_requires=[
        'asreview>=1.2'
    ],
    entry_points={
        'asreview.models.classifiers': [
        ],
        'asreview.models.feature_extraction': [
            'reuseable_sbert = asreviewcontrib.models:reuseable_sbert',
            'reuseable_MiniLM = asreviewcontrib.models:reuseable_MiniLM',

        ],
        'asreview.models.balance': [
        ],
        'asreview.models.query': [
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/jteijema/asreview-reusable-fe/issues',
        'Source': 'https://github.com/jteijema/asreview-reusable-fe/',
    },
)
