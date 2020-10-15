import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="craam-pkg-bmortella",
    version="1.0.0",
    author="Bruno Mortella, Júlia Vitória",
    author_email="bmortella@gmail.com, juliavpaiva@outlook.com",
    description="Package to work with SST and POEMAS data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bmortella/craam",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)