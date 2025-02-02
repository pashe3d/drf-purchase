import re

from setuptools import find_packages, setup

name = 'drf-purchase'
owner = 'xurvan'

with open(f'purchase/__init__.py') as f:
    version = re.search(r'([0-9]+(\.dev|\.|)){3}', f.read()).group(0)

with open('README.md') as f:
    readme = f.read()

setup(
    name=name,
    version=version,
    license='apache-2.0',
    description='Online shopping package for DRF',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=owner.capitalize(),
    url=f'https://github.com/{owner}/{name}',
    download_url=f'https://github.com/{owner}/{name}/archive/v{version}.zip',
    project_urls={
        'Code': f'https://github.com/{owner}/{name}',
        'Issue tracker': f'https://github.com/{owner}/{name}/issues',
    },
    packages=find_packages(),
    install_requires=['django', 'djangorestframework'],
    python_requires='>=3.6',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
