from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLops_Jenkins_Grafana_GCP",
    version="v0.1",
    author="SandeepChowdhury",
    packages=find_packages(),
    install_requires = requirements,
)