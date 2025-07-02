from setuptools import setup, find_packages

setup(
    name='fairsyn',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'sdv',
        'fairlearn',
    ],
    description='Fairness-aware synthetic data generation library',
    author='Your Name',
    license='MIT',
)
