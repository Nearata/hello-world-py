from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hello-world-nearata",
    version="0.0.4",
    author="Nearata",
    author_email="williamdicicco@protonmail.com",
    description="Hello World!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nearata/hello-world-py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)