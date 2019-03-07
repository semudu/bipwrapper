import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bipapi-semudu",
    version="0.0.1",
    author="Serhat Durmaz",
    author_email="serhat.md@gmail.com",
    description="BIP Messanger API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semudu/bipapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
