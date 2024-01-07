from setuptools import find_packages, setup
from glob import glob
import os

package_name = "manipulator_6dof_description"

setup(
    name=package_name,
    version="1.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name, "urdf"), glob("urdf/*.xacro")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Wiktor Bajor",
    maintainer_email="wiktorbajor1@gmail.com",
    description="Description in URDF format of custom 6 DoF",
    license="Apache License 2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [],
    },
)
