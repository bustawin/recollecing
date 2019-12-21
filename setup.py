from pathlib import Path

from setuptools import find_packages, setup

test_requires = ["pytest"]

setup(
    name="recollecing",
    version="0.0.1",
    url="https://github.com/bustawin/recollecing",
    project_urls={
        "Documentation": "https://github.com/bustawin/recollecing",
        "Code": "https://github.com/bustawin/recollecing",
        "Issue tracker": "https://github.com/bustawin/recollecing/issues",
    },
    license="AGPLV3",
    author="Xavier Bustamante Talavera",
    author_email="xavier@bustawin.com",
    description="Make requests's sessions auto-retry on failure.",
    packages=find_packages(),
    python_requires=">=3.6",
    long_description=Path("README.rst").read_text("utf8"),
    install_requires=["requests", "retry-requests", "furl", "click"],
    extras_require={"test": test_requires},
    tests_require=test_requires,
    setup_requires=["pytest-runner"],
    entry_points={
        "console_scripts": ["reco = recollecing.application.cli:recollecing"]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
