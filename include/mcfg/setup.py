from setuptools import setup, find_packages

setup(
    name='mucfg',
    version='0.1.0',
    author='Mustafa Eren BAŞOL',
    author_email='merenbasol@gmail.com',
    description='Configurer for Muzika. This package only avalible on Muzika',
    long_description_content_type='text/markdown',
    url='https://github.com/merenbasol42',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'typing-extensions',  # Tip desteği için
    ],
    extras_require={
        'dev': [
            'pytest',
            'mypy',
        ],
        'test': [
            'pytest',
        ],
    },
    project_urls={
        'Source': 'https://github.com/merenbasol42',
    }, 
)
