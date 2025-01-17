from setuptools import setup, find_packages

# https://pypi.org/search/?q=gressling

setup(
    name='gressling',
    version='0.8',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    author='Gressling, T.',
    author_email='thorsten.gressling@gressling.com',
    description='Cheminformatics toolset for lectures at Humboldt University Berlin with focus on LLM functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
