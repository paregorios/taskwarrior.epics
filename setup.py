import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="taskwarrior.epics",
    version="0.0.1",
    author="Tom Elliott",
    author_email="tom.elliott@nyu.edu",
    description="manage complex projects in taskwarrior using tasks tagged with epic",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['airtight', 'better_exceptions'],
    python_requires='>=3.7.2'
)
