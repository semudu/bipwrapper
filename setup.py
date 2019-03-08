import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bip-api",
    version="0.0.1",
    description="BIP Messenger API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Serhat Durmaz",
    author_email="serhat.md@gmail.com",
    url="https://github.com/semudu/bip-api",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
