from setuptools import setup, find_packages

setup(
    name='exchangeutil',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'layered-yaml-attrdict-config',
        'etaprogress',
    ],
    entry_points="""
    [console_scripts]
    free-exchange-space=exchangeutil.free_exchange_space:main
    """,
)
