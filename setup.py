import os

from setuptools import find_packages, setup


def package_files(where):
    paths = []
    for directory in where:
        for (path, directories, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join(path, filename).replace("src/cwl_wrapper/", ""))
    return paths


extra_files = package_files(["src/cwl_wrapper/assets", "src/cwl_wrapper/tests/data"])
print(extra_files)

console_scripts = []

console_scripts.append("cwl-wrapper=cwl_wrapper.app:main")

# print(find_packages(where='src'))

setup(
    entry_points={"console_scripts": console_scripts},
    packages=(find_packages(where="src")),
    package_dir={"": "src"},
    package_data={"": extra_files},
    test_suite="tests.subworkflow_test_suite",
)
