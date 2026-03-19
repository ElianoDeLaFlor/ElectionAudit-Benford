from setuptools import setup, find_packages

setup(
    name="benford-elections-2020",
    version="0.1",
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'matplotlib', 'scipy'],
    author="Kodjo Setekpo",
    description="Outil d'audit statistique des élections US 2020",
    license="MIT",
)