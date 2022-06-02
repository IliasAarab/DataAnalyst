from setuptools import setup, find_packages
import codecs
import os

about = {}
# with open("src/EDWtoDISC/__about__.py") as f:
#     exec(f.read(), about)


here = os.path.abspath(os.path.dirname(__file__))

# with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Automated data analyst"


setup(
    name="DataAnalyst",
    version=VERSION,
    author="Ilias Aarab",
    author_email="ilias.aarab@ecb.europa.eu",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=DESCRIPTION,
    python_requires=">=3.7, <3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"":"src"},
    packages=find_packages(where= "src")
)
