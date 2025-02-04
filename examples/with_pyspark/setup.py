from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="with_pyspark",
        packages=find_packages(exclude=["with_pyspark_tests"]),
        install_requires=[
            "dagster",
            "dagster-spark",
            "dagster-pyspark",
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )
