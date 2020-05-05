from setuptools import setup, find_packages

setup(
    name="generate_report",
    version="0.0.0",
    packages=find_packages(),
    url="https://github.com/cov-ert/Reports",
    license="MIT",
    entry_points={"console_scripts": ["generate_report = UK_full_report.run_report:main"]},
    test_suite="nose.collector",
    tests_require=["nose >= 1.3"],
    install_requires=[
        "matplotlib==3.2.1",
        "numpy==1.18.1",
        "pweave==0.30.3",
        "scipy==1.4.1",
        "tabulate==0.8.7",
        "pandas==1.0.1",
        "scipy==1.4.1",
        "requests==2.20.0",
        "epiweeks==2.1.1",
        "argparse==1.4.0",
        "geopandas==0.7.0",
        "shapely==1.7.0",
        "descartes==1.1.0",
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
)
