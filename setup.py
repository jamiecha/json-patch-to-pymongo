import setuptools


def get_version():
    version_file = "src/jsonpatch2pymongo/_version.py"
    with open(version_file) as f:
        exec(compile(f.read(), version_file, "exec"))
    return locals()["__version__"]


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonpatch2pymongo",
    version=get_version(),
    author="JungYoon Cha",
    author_email="jamiecha@gmail.com",
    description="Convert JSON patch into pymongo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamiecha/jsonpatch2pymongo",
    project_urls={"Bug Tracker": "https://github.com/jamiecha/jsonpatch2pymongo/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
