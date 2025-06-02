from setuptools import setup, find_packages

setup(
    name="VeloxEngine",
    version="0.1.2",
    author="AynuDaDev",
    description="A minimal SDL2-based game engine in Python for building 2D games quickly.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://pixnox-studio.github.io/Velox-Web/",
    packages=find_packages(),
    install_requires=[
        "pygame-ce",
        "moderngl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",

    ],
    python_requires=">=3.7",
)
