from setuptools import find_packages, setup
import os
from glob import glob

package_name = "manipulator_6dof_bringup"

setup(
    name=package_name,
    version="1.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "launch"), glob("launch/*.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Wiktor Bajor",
    maintainer_email="wiktorbajor1@gmail.com",
    description="Bring up package for custom 6DoF manipulator",
    license="Apache License 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
