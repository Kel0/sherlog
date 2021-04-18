import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sherlogger",
    version="0.0.4",
    author="Kel0",
    author_email="rozovdima123@gmail.com",
    description="Simple logger which can work with network!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kel0/sherlog",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "aiohttp==3.7.4.post0"
    ]
)
