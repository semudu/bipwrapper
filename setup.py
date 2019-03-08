import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bipwrapper",
    version="0.0.2",
    description="BIP Messenger API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Serhat Durmaz",
    author_email="serhat.md@gmail.com",
    url="https://github.com/semudu/bipwrapper",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False
)
