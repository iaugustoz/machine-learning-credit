from setuptools import setup, find_packages

setup(
    name='machine-learning-credit',
    version='1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'plotly',
        'matplotlib',
        'seaborn',
    ],
)
