from setuptools import setup, find_packages

setup(
    name="pkl_viewer",
    version="0.1.0",
    description="A simple GUI to open and view .pkl files using Tkinter",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pkl-viewer=pkl_viewer.main:run_gui"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
