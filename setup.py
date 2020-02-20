import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bipwrapper",
    version="1.0.1",
    description="BIP Messenger API Wrapper",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Serhat Durmaz",
    author_email="serhat.md@gmail.com",
    url="https://github.com/semudu/bipwrapper",
    download_url="https://github.com/semudu/bipwrapper/archive/v1.0.1.tar.gz",
    keywords=["BIP", "WRAPPER", "API"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
