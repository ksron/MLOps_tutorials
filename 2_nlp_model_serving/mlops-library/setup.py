from setuptools import setup

setup(
    name="nlp_mlopslib",
    version="0.0.1",
    description="MLOps library for NLP model",
    url="https://github.com/ksron/MLOps_tutorials.git",
    author="ksron",
    packages=["mlopslib"],
    install_requires=[
        "google-cloud-storage==2.16.0"
    ]
)