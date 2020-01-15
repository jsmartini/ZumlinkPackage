import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsmartini", # Replace with your own username
    version="0.0.1",
    author="Jonathan Martini",
    author_email="jsmartini@crimson.ua.edu",
    description="Zumlink IOT radio for Z9-C/-T",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)