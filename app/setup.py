from setuptools import setup, find_packages

setup(
    name='website',
    packages=find_packages(),
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
