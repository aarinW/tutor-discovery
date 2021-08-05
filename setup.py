import io
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()

about = {}
with io.open(os.path.join(here, "tutordiscovery", "__about__.py"), "rt", encoding="utf-8") as f:
    exec(f.read(), about)


setup(
    name="tutor-discovery",
    version=about["__version__"],
    url="https://docs.tutor.overhang.io/",
    project_urls={
        "Documentation": "https://docs.tutor.overhang.io/",
        "Code": "https://github.com/overhangio/tutor-discovery",
        "Issue tracker": "https://github.com/overhangio/tutor-discovery/issues",
        "Community": "https://discuss.overhang.io",
    },
    license="AGPLv3",
    author="Overhang.io",
    author_email="contact@overhang.io",
    description="A Tutor plugin for course discovery, the Open edX service for providing access to consolidated course and program metadata",
    long_description=readme,
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=["tutor>=12.0.0,<13.0.0"],
    python_requires=">=3.5",
    entry_points={"tutor.plugin.v0": ["discovery = tutordiscovery.plugin"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)