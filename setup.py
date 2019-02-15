import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfer",
    version="0.0.1",
    author="Davy Guo, Gabriel Bogo, Makk, Yuwei Liu",
    author_email="",
    description="Implementation of the `infer` R package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UBC-MDS/pyfer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pandas',
          'pytest',
    ],
)
