from setuptools import setup, find_packages

setup(
    name='image_processing_package',
    version='0.1.0',
    description='A Python package for image processing tasks including comparison, histogram matching, resizing, and visualization.',
    author='Jefter Alexandre',
    author_email='jefteralexandre73@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.24.3',
        'scikit-image>=0.22.0',
        'matplotlib>=3.7.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
